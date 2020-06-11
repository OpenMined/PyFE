import numpy
from charm.toolbox.pairinggroup import ZR

from pyfe.encrypted_vector import EncryptedVector
from pyfe.utils import fast_exp_const_time


class Encryptor:
    def __init__(self, context, public_key):

        self.context = context
        self.public_key = public_key

    def encrypt(self, plain_vector):
        """
        Encrypts the vector object and generates EncryptedVector
        Args:
            plain_vector: data to be encrypted
        """

        vector = numpy.array(
            plain_vector, dtype=numpy.int64
        )  # dtype is just to convert float to int

        assert (
            len(self.public_key) == len(vector) + 1
        ), 'Vector has length {}, key is for length {}.'.format(
            len(vector), len(self.public_key) - 1
        )

        v_min = numpy.min(vector).item()
        v_max = numpy.max(vector).item()

        gamma = self.context.group.random(ZR)
        a = self.context.group.random(ZR)
        b = self.context.group.random(ZR)
        c = self.context.group.random(ZR)
        d = self.context.group.random(ZR)
        det = a * d - b * c
        assert det != 0
        inv_a = d / det
        inv_b = -b / det
        inv_c = -c / det
        inv_d = a / det

        g1_inva = self.context.g1 ** inv_a
        g1_invb = self.context.g1 ** inv_b
        g2_a = self.context.g2 ** a
        g2_c = self.context.g2 ** c
        exp_g1_inva = fast_exp_const_time(g1_inva, vector, v_min, v_max)
        exp_g1_invb = fast_exp_const_time(g1_invb, vector, v_min, v_max)
        exp_g2_a = fast_exp_const_time(g2_a, vector, v_min, v_max)
        exp_g2_c = fast_exp_const_time(g2_c, vector, v_min, v_max)
        left = [  # bias term
            [
                g1_inva * (self.public_key.h1[0] ** (gamma * inv_c)),
                g1_invb * (self.public_key.h1[0] ** (gamma * inv_d)),
            ]
        ]
        right = [  # bias term
            [g2_a * (self.public_key.h2[0] ** (-b)), g2_c * (self.public_key.h2[0] ** (-d))]
        ]
        for i in range(1, self.public_key.n):
            left.append(
                [
                    exp_g1_inva[i - 1] * (self.public_key.h1[i] ** (gamma * inv_c)),
                    exp_g1_invb[i - 1] * (self.public_key.h1[i] ** (gamma * inv_d)),
                ]
            )
            right.append(
                [
                    exp_g2_a[i - 1] * (self.public_key.h2[i] ** (-b)),
                    exp_g2_c[i - 1] * (self.public_key.h2[i] ** (-d)),
                ]
            )
        return EncryptedVector(
            group=self.context.group, simplifier=self.context.g1 ** gamma, left=left, right=right,
        )
