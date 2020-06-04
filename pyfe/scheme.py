import numpy

from charm.toolbox.pairinggroup import PairingGroup, ZR, G1, G2, pair

from pyfe.keys import PublicKey, MasterKey
from pyfe.utils import fast_exp_const_time
from pyfe.vectors import EncryptedVector

class Scheme:
    """
    Scheme is the class that setups the public and master key, and also
    generates secret key for function evaluation(pending). It holds the method that encrypts
    the vector
    """

    def __init__(self):
        """
        Initiate the Scheme object
        """

        self.group = PairingGroup('MNT159')

        self.g1 = self.group.random(G1)
        self.g2 = self.group.random(G2)

        self.gt = pair(self.g1, self.g2)

    def setup(self, vector_length=1):
        """
        Generates the public key and the master key
        """

        assert vector_length>0, "Vector size must be positive"

        s = [self.group.random(ZR) for i in range(vector_length+1)]
        t = [self.group.random(ZR) for i in range(vector_length+1)]
        h1 = [self.g1 ** si for si in s]
        h2 = [self.g2 ** ti for ti in t]

        pk = PublicKey(self.group, h1, h2)
        msk = MasterKey(pk, s, t)

        return (pk, msk)

    def encrypt(self, pk, plain_vector):
        """
        Encrypts the vector object and generates EncryptedVector
        Args:
            pk: PublicKey, public key to be used for encryption
            vector: Vector, data to be encrypted
        """

        vector = numpy.array(plain_vector, dtype=numpy.int64) #dtype is just to convert float to int

        assert (
            len(pk) == len(vector) + 1
        ), (
            'Vector has length {}, key is for length {}.'.format(
                len(vector),
                len(pk) - 1
            )
        )

        v_min = numpy.min(vector).item()
        v_max = numpy.max(vector).item()

        gamma = self.group.random(ZR)
        a = self.group.random(ZR)
        b = self.group.random(ZR)
        c = self.group.random(ZR)
        d = self.group.random(ZR)
        det = a * d - b * c
        assert det != 0
        inv_a = d / det
        inv_b = -b / det
        inv_c = -c / det
        inv_d = a / det

        g1_inva = self.g1 ** inv_a
        g1_invb = self.g1 ** inv_b
        g2_a = self.g2 ** a
        g2_c = self.g2 ** c
        exp_g1_inva = fast_exp_const_time(g1_inva, vector, v_min, v_max)
        exp_g1_invb = fast_exp_const_time(g1_invb, vector, v_min, v_max)
        exp_g2_a = fast_exp_const_time(g2_a, vector, v_min, v_max)
        exp_g2_c = fast_exp_const_time(g2_c, vector, v_min, v_max)
        left = [  # bias term
            [
                g1_inva * (pk.h1[0] ** (gamma * inv_c)),
                g1_invb * (pk.h1[0] ** (gamma * inv_d))
            ]
        ]
        right = [  # bias term
            [
                g2_a * (pk.h2[0] ** (-b)),
                g2_c * (pk.h2[0] ** (-d))
            ]
        ]
        for i in range(1, pk.n):
            left.append(
                [
                    exp_g1_inva[i-1] * (pk.h1[i] ** (gamma * inv_c)),
                    exp_g1_invb[i-1] * (pk.h1[i] ** (gamma * inv_d))
                ]
            )
            right.append(
                [
                    exp_g2_a[i-1] * (pk.h2[i] ** (-b)),
                    exp_g2_c[i-1] * (pk.h2[i] ** (-d))
                ]
            )
        return EncryptedVector(
            group=self.group,
            simplifier=self.g1 ** gamma,
            left=left,
            right=right,
        )
