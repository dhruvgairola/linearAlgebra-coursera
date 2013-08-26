# version code 941
# Please fill out this stencil and submit using the provided submission script.

from vecutil import list2vec
from solver import solve
from triangular import triangular_solve
from matutil import listlist2mat, coldict2mat
import matutil
from mat import Mat
from GF2 import one
from vec import Vec
import independence
import hw4


## Problem 1
w0 = list2vec([1,0,0])
w1 = list2vec([0,1,0])
w2 = list2vec([0,0,1])

v0 = list2vec([1,2,3])
v1 = list2vec([1,3,3])
v2 = list2vec([0,3,3])

# Fill in exchange_S1 and exchange_S2
# with appropriate lists of 3 vectors

exchange_S0 = [w0, w1, w2]
exchange_S1 = [w0, w1, v0]
exchange_S2 = [w0, v0, v2]
exchange_S3 = [v0, v1, v2]



## Problem 2
w0 = list2vec([0,one,0])
w1 = list2vec([0,0,one])
w2 = list2vec([one,one,one])

v0 = list2vec([one,0,one])
v1 = list2vec([one,0,0])
v2 = list2vec([one,one,0])

exchange_2_S0 = [w0, w1, w2]
exchange_2_S1 = [w0, w1, v0]
exchange_2_S2 = [w1, v0, v2]
exchange_2_S3 = [v0, v1, v2]



## Problem 3
def morph(S, B):
    '''
    Input:
        - S: a list of distinct Vec instances
        - B: a list of linearly independent Vec instances
        - Span S == Span B
    Output: a list of pairs of vectors to inject and eject
    Example:
        >>> #This is how our morph works.  Yours may yield different results.
        >>> S = [list2vec(v) for v in [[1,0,0],[0,1,0],[0,0,1]]]
        >>> B = [list2vec(v) for v in [[1,1,0],[0,1,1],[1,0,1]]]
        >>> morph(S, B)
        [(Vec({0, 1, 2},{0: 1, 1: 1, 2: 0}), Vec({0, 1, 2},{0: 1, 1: 0, 2: 0})), (Vec({0, 1, 2},{0: 0, 1: 1, 2: 1}), Vec({0, 1, 2},{0: 0, 1: 1, 2: 0})), (Vec({0, 1, 2},{0: 1, 1: 0, 2: 1}), Vec({0, 1, 2},{0: 0, 1: 0, 2: 1}))]

    '''
    T = []
    M = []
    C = S.copy()

    for b in B:
        t1 = hw4.exchange(C, T, b)

        T.append(b)
        C.remove(t1)
        C.append(b)
        M.append((b, t1))

    return M

## Problem 4
# Please express each solution as a list of vectors (Vec instances)

row_space_1 = [Vec({0, 1, 2},{0: 1, 1: 2, 2: 0}), Vec({0, 1, 2},{0: 0, 1: 1, 2: 2})]
col_space_1 = [Vec({0, 1},{0: 1, 1: 0}), Vec({0, 1},{0: 0, 1: 1})]

row_space_2 = [Vec({0, 1, 2, 3},{0: 1, 1: 4, 2: 0, 3: 0}), Vec({0, 1, 2, 3},{0: 0, 1: 2, 2: 2, 3: 0}), Vec({0, 1, 2, 3},{0: 0, 1: 0, 2: 1, 3: 1})]
col_space_2 = [Vec({0, 1, 2},{0: 1, 1: 0, 2: 0}), Vec({0, 1, 2},{0: 0, 1: 2, 2: 1}), Vec({0, 1, 2},{0: 0, 1: 0, 2: 1})]

row_space_3 = [Vec({0},{0: 1})]
col_space_3 = [Vec({0, 1, 2},{0: 1, 1: 2, 2: 3})]

row_space_4 = [Vec({0, 1},{0: 1, 1: 0}), Vec({0, 1},{0: 2, 1: 1})]
col_space_4 = [Vec({0, 1, 2},{0: 1, 1: 2, 2: 3}), Vec({0, 1, 2},{0: 0, 1: 1, 2: 4})]



## Problem 5
def my_is_independent(L): 
    '''
    input:  A list, L, of Vecs
    output: A boolean indicating if the list is linearly independent
    
    >>> L = [Vec({0, 1, 2},{0: 1, 1: 0, 2: 0}), Vec({0, 1, 2},{0: 0, 1: 1, 2: 0}), Vec({0, 1, 2},{0: 0, 1: 0, 2: 1}), Vec({0, 1, 2},{0: 1, 1: 1, 2: 1}), Vec({0, 1, 2},{0: 1, 1: 1, 2: 0}), Vec({0, 1, 2},{0: 0, 1: 1, 2: 1})]
    >>> my_is_independent(L)
    False
    >>> my_is_independent(L[:2])
    True
    >>> my_is_independent(L[:3])
    True
    >>> my_is_independent(L[1:4])
    True
    >>> my_is_independent(L[0:4])
    False
    >>> my_is_independent(L[2:])
    False
    >>> my_is_independent(L[2:5])
    False
    '''
    return len(L) == independence.rank(L)


## Problem 6
def subset_basis(T): 
    '''
    input: A list, T, of Vecs
    output: A list, S, containing Vecs from T, that is a basis for the
    space spanned by T.
    
    >>> a0 = Vec({'a','b','c','d'}, {'a':1})
    >>> a1 = Vec({'a','b','c','d'}, {'b':1})
    >>> a2 = Vec({'a','b','c','d'}, {'c':1})
    >>> a3 = Vec({'a','b','c','d'}, {'a':1,'c':3})
    >>> subset_basis([a0,a1,a2,a3]) == [Vec({'c', 'b', 'a', 'd'},{'a': 1}), Vec({'c', 'b', 'a', 'd'},{'b': 1}), Vec({'c', 'b', 'a', 'd'},{'c': 1})]
    True
    '''

    S = []

    for i, l in enumerate(T):
        S.append(l)
        if hw4.is_superfluous(S, len(S)-1):
            S.remove(l)

    return S


## Problem 7
def my_rank(L): 
    '''
    input: A list, L, of Vecs
    output: The rank of the list of Vecs
    
    >>> my_rank([list2vec(v) for v in [[1,2,3],[4,5,6],[1.1,1.1,1.1]]])
    2
    '''
    return len(subset_basis(L))


## Problem 8
# Please give each answer as a boolean

only_share_the_zero_vector_1 = True
only_share_the_zero_vector_2 = True
only_share_the_zero_vector_3 = True



## Problem 9
def direct_sum_decompose(U_basis, V_basis, w):
    '''
    input:  A list of Vecs, U_basis, containing a basis for a vector space, U.
    A list of Vecs, V_basis, containing a basis for a vector space, V.
    A Vec, w, that belongs to the direct sum of these spaces.
    output: A pair, (u, v), such that u+v=w and u is an element of U and
    v is an element of V.
    
    >>> U_basis = [Vec({0, 1, 2, 3, 4, 5},{0: 2, 1: 1, 2: 0, 3: 0, 4: 6, 5: 0}), Vec({0, 1, 2, 3, 4, 5},{0: 11, 1: 5, 2: 0, 3: 0, 4: 1, 5: 0}), Vec({0, 1, 2, 3, 4, 5},{0: 3, 1: 1.5, 2: 0, 3: 0, 4: 7.5, 5: 0})]
    >>> V_basis = [Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: 7, 3: 0, 4: 0, 5: 1}), Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: 15, 3: 0, 4: 0, 5: 2})]
    >>> w = Vec({0, 1, 2, 3, 4, 5},{0: 2, 1: 5, 2: 0, 3: 0, 4: 1, 5: 0})
    >>> direct_sum_decompose(U_basis, V_basis, w) == (Vec({0, 1, 2, 3, 4, 5},{0: 2.0, 1: 4.999999999999972, 2: 0.0, 3: 0.0, 4: 1.0, 5: 0.0}), Vec({0, 1, 2, 3, 4, 5},{0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0}))
    True
    '''
    combined = U_basis + V_basis
    separation_boundary = len(U_basis)
    soln = solve(coldict2mat(combined), w)

    u = Vec(w.D, {})
    v = Vec(w.D, {})

    for key, val in soln.f.items():
        if key < separation_boundary:
            u += val * U_basis[key]
        else:
            v += val * combined[key]

    return (u, v)

## Problem 10
def is_invertible(M): 
    '''
    input: A matrix, M
    outpit: A boolean indicating if M is invertible.
    
    >>> M = Mat(({0, 1, 2, 3}, {0, 1, 2, 3}), {(0, 1): 0, (1, 2): 1, (3, 2): 0, (0, 0): 1, (3, 3): 4, (3, 0): 0, (3, 1): 0, (1, 1): 2, (2, 1): 0, (0, 2): 1, (2, 0): 0, (1, 3): 0, (2, 3): 1, (2, 2): 3, (1, 0): 0, (0, 3): 0})
    >>> is_invertible(M)
    True
    '''
    nullspace = solve(M, list2vec([0]))
    ker_zero = nullspace == Vec(nullspace.D, {})

    im_f_eq_codomain = independence.rank(subset_basis(matutil.mat2coldict(M).values())) == len(M.D[1])

    # invertible if its one-to-one, onto, and square matrix
    return ker_zero and im_f_eq_codomain and len(matutil.mat2coldict(M)) == len(matutil.mat2rowdict(M))


## Problem 11
def find_matrix_inverse(A):
    '''
    input: An invertible matrix, A, over GF(2)
    output: Inverse of A

    >>> M = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): one, (1, 2): 0, (0, 0): 0, (2, 0): 0, (1, 0): one, (2, 2): one, (0, 2): 0, (2, 1): 0, (1, 1): 0})
    >>> find_matrix_inverse(M) == Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): one, (2, 0): 0, (0, 0): 0, (2, 2): one, (1, 0): one, (1, 2): 0, (1, 1): 0, (2, 1): 0, (0, 2): 0})
    True
    '''
    R = len(A.D[0])
    C = len(A.D[1])
    coldict = {}
    for i in range(C):
        b = [0] * R
        b[i] = one
        s = solve(A, list2vec(b))
        coldict[i] = s

    return coldict2mat(coldict)


## Problem 12
def find_triangular_matrix_inverse(A): 
    '''
    input: An upper triangular Mat, A, with nonzero diagonal elements
    output: Inverse of A
    >>> A = listlist2mat([[1, .5, .2, 4],[0, 1, .3, .9],[0,0,1,.1],[0,0,0,1]])
    >>> find_triangular_matrix_inverse(A) == Mat(({0, 1, 2, 3}, {0, 1, 2, 3}), {(0, 1): -0.5, (1, 2): -0.3, (3, 2): 0.0, (0, 0): 1.0, (3, 3): 1.0, (3, 0): 0.0, (3, 1): 0.0, (2, 1): 0.0, (0, 2): -0.05000000000000002, (2, 0): 0.0, (1, 3): -0.87, (2, 3): -0.1, (2, 2): 1.0, (1, 0): 0.0, (0, 3): -3.545, (1, 1): 1.0})
    True
    '''

    R = len(A.D[0])
    C = len(A.D[1])
    coldict = {}
    for i in range(C):
        b = [0] * R
        b[i] = 1
        s = triangular_solve(list(matutil.mat2rowdict(A).values()), list(A.D[0]), list2vec(b))
        coldict[i] = s

    return coldict2mat(coldict)



# import hw5
# import hw4
# from mat import Mat
# import vecutil
# import matutil
# from vec import Vec
# from GF2 import one
# L = [Vec({0, 1, 2},{0: 1, 1: 0, 2: 0}), Vec({0, 1, 2},{0: 0, 1: 1, 2: 0}), Vec({0, 1, 2},{0: 0, 1: 0, 2: 1}), Vec({0, 1, 2},{0: 1, 1: 1, 2: 1}), Vec({0, 1, 2},{0: 1, 1: 1, 2: 0}), Vec({0, 1, 2},{0: 0, 1: 1, 2: 1})]
# hw5.my_is_independent(L)
# hw5.my_is_independent(L[:2])
# S = [vecutil.list2vec(v) for v in [[1,0,0],[0,1,0],[0,0,1]]]
# B = [vecutil.list2vec(v) for v in [[1,1,0],[0,1,1],[1,0,1]]]
# ff = hw5.morph(S, B)
# ff == [(Vec({0, 1, 2},{0: 1, 1: 1, 2: 0}), Vec({0, 1, 2},{0: 1, 1: 0, 2: 0})), (Vec({0, 1, 2},{0: 0, 1: 1, 2: 1}), Vec({0, 1, 2},{0: 0, 1: 1, 2: 0})), (Vec({0, 1, 2},{0: 1, 1: 0, 2: 1}), Vec({0, 1, 2},{0: 0, 1: 0, 2: 1}))]
# a0 = Vec({'a','b','c','d'}, {'a':1})
# a1 = Vec({'a','b','c','d'}, {'b':1})
# a2 = Vec({'a','b','c','d'}, {'c':1})
# a3 = Vec({'a','b','c','d'}, {'a':1,'c':3})
# sb = hw5.subset_basis([a0,a1,a2,a3])
# sb == [Vec({'c', 'b', 'a', 'd'},{'a': 1}), Vec({'c', 'b', 'a', 'd'},{'b': 1}), Vec({'c', 'b', 'a', 'd'},{'c': 1})]
# U_basis = [Vec({0, 1, 2, 3, 4, 5},{0: 2, 1: 1, 2: 0, 3: 0, 4: 6, 5: 0}), Vec({0, 1, 2, 3, 4, 5},{0: 11, 1: 5, 2: 0, 3: 0, 4: 1, 5: 0}), Vec({0, 1, 2, 3, 4, 5},{0: 3, 1: 1.5, 2: 0, 3: 0, 4: 7.5, 5: 0})]
# V_basis = [Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: 7, 3: 0, 4: 0, 5: 1}), Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: 15, 3: 0, 4: 0, 5: 2})]
# w = Vec({0, 1, 2, 3, 4, 5},{0: 2, 1: 5, 2: 0, 3: 0, 4: 1, 5: 0})
# ss = hw5.direct_sum_decompose(U_basis, V_basis, w)
# ss == (Vec({0, 1, 2, 3, 4, 5},{0: 2.0, 1: 4.999999999999972, 2: 0.0, 3: 0.0, 4: 1.0, 5: 0.0}), Vec({0, 1, 2, 3, 4, 5},{0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0}))
# M = Mat(({0, 1, 2, 3}, {0, 1, 2, 3}), {(0, 1): 0, (1, 2): 1, (3, 2): 0, (0, 0): 1, (3, 3): 4, (3, 0): 0, (3, 1): 0, (1, 1): 2, (2, 1): 0, (0, 2): 1, (2, 0): 0, (1, 3): 0, (2, 3): 1, (2, 2): 3, (1, 0): 0, (0, 3): 0})
# hw5.is_invertible(M)
# A = Mat(({0, 1}, {0, 1, 2}), {(0, 1): 2, (1, 2): 1, (0, 0): 1, (1, 0): 3, (0, 2): 3, (1, 1): 1})
# B = Mat(({0, 1, 2, 3}, {0, 1, 2, 3}), {(0, 1): 0, (1, 2): 1, (3, 2): 0, (0, 0): 1, (3, 3): 4, (3, 0): 0, (3, 1): 0, (1, 1): 2, (2, 1): 0, (0, 2): 1, (2, 0): 0, (1, 3): 0, (2, 3): 1, (2, 2): 3, (1, 0): 0, (0, 3): 0})
# C = Mat(({0, 1, 2}, {0, 1}), {(0, 1): 0, (2, 0): 2, (0, 0): 1, (1, 0): 0, (1, 1): 1, (2, 1): 1})
# D = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): 5, (1, 2): 2, (0, 0): 1, (2, 0): 4, (1, 0): 2, (2, 2): 7, (0, 2): 8, (2, 1): 6, (1, 1): 5})
# E = Mat(({0, 1, 2, 3, 4}, {0, 1, 2, 3, 4}), {(1, 2): 7, (3, 2): 7, (0, 0): 3, (3, 0): 1, (0, 4): 3, (1, 4): 2, (1, 3): 4, (2, 3): 0, (2, 1): 56, (2, 4): 5, (4, 2): 6, (1, 0): 2, (0, 3): 7, (4, 0): 2, (0, 1): 5, (3, 3): 4, (4, 1): 4, (3, 1): 23, (4, 4): 5, (0, 2): 7, (2, 0): 2, (4, 3): 8, (2, 2): 9, (3, 4): 2, (1, 1): 4})
# M = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): one, (1, 2): 0, (0, 0): 0, (2, 0): 0, (1, 0): one, (2, 2): one, (0, 2): 0, (2, 1): 0, (1, 1): 0})
# hw5.find_matrix_inverse(M) == Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): one, (2, 0): 0, (0, 0): 0, (2, 2): one, (1, 0): one, (1, 2): 0, (1, 1): 0, (2, 1): 0, (0, 2): 0})
# A = matutil.listlist2mat([[1, .5, .2, 4],[0, 1, .3, .9],[0,0,1,.1],[0,0,0,1]])
# hw5.find_triangular_matrix_inverse(A) == Mat(({0, 1, 2, 3}, {0, 1, 2, 3}), {(0, 1): -0.5, (1, 2): -0.3, (3, 2): 0.0, (0, 0): 1.0, (3, 3): 1.0, (3, 0): 0.0, (3, 1): 0.0, (2, 1): 0.0, (0, 2): -0.05000000000000002, (2, 0): 0.0, (1, 3): -0.87, (2, 3): -0.1, (2, 2): 1.0, (1, 0): 0.0, (0, 3): -3.545, (1, 1): 1.0})