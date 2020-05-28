from pyfe.utils import is_array, is_scalar

# TODO: Get rid of Vector class
class Vector:
    def __init__(self, array=None):
        """
        Simple class that wraps the data
        """
        assert array is not None
        assert is_array(array), "Wrong Input array"
        assert (len(array) > 0), 'Vector length should be non zero'

        self.n = len(array)
        self.content = []
        for s in array:
            assert is_scalar(s), "Input doesn't contain vaild scalars"
            self.content.append(int(s))


    def min(self):
        return min(self.content)

    def max(self):
        return max(self.content)


class EncryptedVector:
    """
        Encrption of vector  
    """
    def __init__(self, group=None, simplifier=None, left=None, right=None):
        assert left
        assert right
        assert group
        assert simplifier
        assert is_array(left)
        assert is_array(right)
        assert (
            len(left) == len(right)
        ), (
            'Ciphertext was not properly generated.'
        )
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
