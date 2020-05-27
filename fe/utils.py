import collections
import numpy as np

def is_array(a):
    return isinstance(a, (collections.Sequence, np.ndarray, list))


def is_scalar(s):
    return (isinstance(s, int) or
            isinstance(s, np.int64) or
            (isinstance(s, float) and s.is_integer()))


def sign(x):
    return (1, -1)[x>0]


def exp(g, x):
    return (g ** abs(x)) ** sign(x)


def fast_exp_const_time(g, X, xmin=0, xmax=255):
    curr = exp(g, xmin)
    precomp = [curr]
    for i in range(xmax-xmin):
        curr *= g
        precomp.append(curr)

    return [precomp[x-xmin] for x in X]
