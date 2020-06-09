from pyfe.utils import is_array


class EncryptedVector:
    """
    Data-structure to store the encryption of the vector.
    """

    def __init__(self, group=None, simplifier=None, left=None, right=None):
        assert left
        assert right
        assert group
        assert simplifier
        assert is_array(left)
        assert is_array(right)
        assert len(left) == len(right), 'Ciphertext was not properly generated.'
        assert len(left) > 1, 'Ciphertext is empty.'
        assert (is_array(x) for x in left)
        assert (is_array(x) for x in right)
        assert (len(x) == 2 for x in left)
        assert (len(x) == 2 for x in right)

        self.n = len(left)
        self.group = group
        self.simplifier = simplifier
        self.left = left
        self.right = right
