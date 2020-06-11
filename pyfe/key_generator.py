from charm.toolbox.pairinggroup import ZR

from pyfe.master_key import MasterKey
from pyfe.public_key import PublicKey


class KeyGenerator:
    """
    Generate the public key and master key.
    """

    def __init__(self, context):
        self.context = context

    def setup(self, vector_length):
        """
        Generates the public key and the master key.
        """
        assert vector_length > 0, 'Vector size must be positive'

        s = [self.context.group.random(ZR) for i in range(vector_length + 1)]
        t = [self.context.group.random(ZR) for i in range(vector_length + 1)]
        h1 = [self.context.g1 ** si for si in s]
        h2 = [self.context.g2 ** ti for ti in t]

        pk = PublicKey(self.context.group, h1, h2)
        msk = MasterKey(pk, s, t)

        return (pk, msk)
