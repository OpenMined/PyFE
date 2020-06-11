from charm.toolbox.pairinggroup import G1
from charm.toolbox.pairinggroup import G2
from charm.toolbox.pairinggroup import PairingGroup
from charm.toolbox.pairinggroup import pair


class Context:
    def __init__(self):
        self.group = PairingGroup('MNT159')

        self.g1 = self.group.random(G1)
        self.g2 = self.group.random(G2)

        self.gt = pair(self.g1, self.g2)
