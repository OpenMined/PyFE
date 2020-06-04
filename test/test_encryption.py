import numpy as np
from pyfe.scheme import Scheme
from pyfe.vectors import EncryptedVector

def test_encryption():
    """
        Test encryption of list and numpy array
    """
    scheme = Scheme()

    x = [1,2,3,4]

    pk, msk = scheme.setup(vector_length=len(x))
    x_enc = scheme.encrypt(pk, x)

    # This is purely observational, just for sake of having a test case
    # TODO: Add robust test case
    assert isinstance(x_enc, EncryptedVector)
    assert x_enc.n - len(x) == 1

    x = np.array([1.,2.,3.])

    # We can reuse the scheme
    pk, msk = scheme.setup(vector_length=len(x))
    x_enc = scheme.encrypt(pk, x)

    assert isinstance(x_enc, EncryptedVector)
    assert x_enc.n - len(x) == 1
