from charm.toolbox.pairinggroup import PairingGroup, G1, G2, pair

class  Context:
    def __init__(self):
        self.group = PairingGroup('MNT159')

        self.g1 = self.group.random(G1)
        self.g2 = self.group.random(G2)

        self.gt = pair(self.g1, self.g2)
