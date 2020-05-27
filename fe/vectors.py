from utils import is_array, is_scalar

class Vector:
    def __init__(self, array=None):
        assert array
        assert is_array(array), "Wrong Input array"
        assert (len(array) > 0), 'Trying to generate an image from an empty vector.'

        self.n = len(array)
        self.content = []
        for s in array:
            assert is_scalar(s), "Input doesn't contain vaild scalars"
            self.content.append(s)


class EncryptedVector:
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
