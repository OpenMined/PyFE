class PublicKey:
    def __init__(self, group=None, h1=None, h2=None):
        self.group = group
        self.n = len(h1)
        self.h1 = h1
        self.h2 = h2


class MasterKey(PublicKey):
    def __init__(self, pk=None, s=None, t=None):
        super(MasterKey, self).__init__(pk.group, pk.h1, pk.h2)
        #assertions here
        self.s = s
        self.t = t
