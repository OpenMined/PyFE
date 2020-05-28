import numpy as np

from pyfe.vectors import Vector
from pyfe.scheme import Scheme

def test_encryption():
    """
    Test encryption of list and numpy array
    """
    scheme = Scheme()

    x = [1,2,3,4]
    v = Vector(x)

    pk, msk = scheme.setup(vector_length=v.n)
    v_enc = scheme.encrypt(pk, v)

    # This is purely observational, just for sake of having a test case
    # TODO: Add robust test case
    assert v_enc.n - v.n == 1

    x = np.array([1.,2.,3.])
    v = Vector(x)

    # We can reuse the scheme
    pk, msk = scheme.setup(vector_length=v.n)
    v_enc = scheme.encrypt(pk, v)

    assert v_enc.n - v.n == 1
