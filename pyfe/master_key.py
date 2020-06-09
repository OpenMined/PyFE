from pyfe.public_key import PublicKey


class MasterKey(PublicKey):
    """
    Holds the master key used to generate the secret key that evaluates the
    function.
    """

    def __init__(self, pk=None, s=None, t=None):
        super(MasterKey, self).__init__(pk.group, pk.h1, pk.h2)
        # assertions here
        self.s = s
        self.t = t
