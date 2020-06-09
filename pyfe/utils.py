import collections

import numpy as np


def is_array(a):
    return isinstance(a, (collections.Sequence, np.ndarray, list))


def sign(x):
    return (1, -1)[x > 0]


def exp(g, x):
    return (g ** abs(x)) ** sign(x)


def fast_exp_const_time(g, X, xmin, xmax):
    """
    Pre-computes the exponents of g and returns required exponents of based on
    X.
    """
    curr = exp(g, xmin)
    precomp = [curr]
    for i in range(xmax - xmin):
        curr *= g
        precomp.append(curr)

    return [precomp[x - xmin] for x in X]
