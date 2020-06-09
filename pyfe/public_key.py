class PublicKey:
    def __init__(self, group=None, h1=None, h2=None):
        """
        Holds the public key used for encryption.
        """
        self.group = group
        self.n = len(h1)
        self.h1 = h1
        self.h2 = h2

    def __len__(self):
        return self.n
