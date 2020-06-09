import numpy as np

from pyfe.context import Context
from pyfe.key_generator import KeyGenerator
from pyfe.encryptor import Encryptor
from pyfe.encrypted_vector import EncryptedVector

def test_encryption():
    """
        Test encryption of list and numpy array
    """
    context = Context()

    x = [1,2,3,4]

    key_generator = KeyGenerator(context)
    pk, msk = key_generator.setup(vector_length=len(x))

    encryptor = Encryptor(context, pk)
    x_enc = encryptor.encrypt(x)

    # This is purely observational, just for sake of having a test case
    # TODO: Add robust test case
    assert isinstance(x_enc, EncryptedVector)
    assert x_enc.n - len(x) == 1

    x = np.array([1.,2.,3.])

    key_generator = KeyGenerator(context)
    pk, msk = key_generator.setup(vector_length=len(x))

    encryptor = Encryptor(context, pk)
    x_enc = encryptor.encrypt(x)

    assert isinstance(x_enc, EncryptedVector)
    assert x_enc.n - len(x) == 1
