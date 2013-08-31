from orthogonalization import orthogonalize,project_orthogonal,aug_orthogonalize
from math import sqrt
from vec import Vec

def orthonormalize(L):
    '''
    Input: a list L of linearly independent Vecs
    Output: A list T of orthonormal Vecs such that for all i in [1, len(L)],
            Span L[:i] == Span T[:i]
    '''
    o = orthogonalize(L)
    l = [sqrt(square_norm(v)) for v in o]
    return [v/l[k] for k, v in enumerate(o)]

def square_norm(v):
    return v * v

def aug_orthonormalize(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - A pair Qlist, Rlist such that:
            * coldict2mat(L) == coldict2mat(Qlist) * coldict2mat(Rlist)
            * Qlist = orthonormalize(L)
    '''
    Q, R = aug_orthogonalize(L)
    Qlist = orthonormalize(Q)
    multipliers = [sqrt(square_norm(q)) for q in Q]
    Rlist = [adjust(r, multipliers) for r in R]
    return (Qlist, Rlist)


def adjust(v, multipliers):
    return Vec(v.D, {k: (multipliers[k] * v) for k, v in v.f.items()})