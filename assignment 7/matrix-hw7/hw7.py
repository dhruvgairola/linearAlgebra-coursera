# version code 1049
# Please fill out this stencil and submit using the provided submission script.

from orthogonalization import orthogonalize,project_orthogonal
import orthonormalization
from mat import Mat,transpose
from vec import Vec
from vecutil import list2vec, zero_vec
from matutil import listlist2mat,mat2rowdict,mat2coldict
from QR import factor
from triangular import triangular_solve
from solver import solve


## Problem 1
def basis(vlist):
    '''
    Input:
        - vlist: a list of Vecs
    Output:
        - a list of linearly independent Vecs with equal span to vlist
    '''
    return [v for v in orthogonalize(vlist) if square_norm(v) > 1E-20]

def square_norm(v):
    return v * v

## Problem 2
def subset_basis(vlist):
    '''
    Input:
        - vlist: a list of Vecs
    Output:
        - linearly independent subset of vlist with the same span as vlist
    '''
    return [vlist[k] for k, v in enumerate(orthogonalize(vlist)) if square_norm(v) > 1E-20]



## Problem 3
def orthogonal_vec2rep(Q, b):
    '''
    Input:
        - Q: an orthogonal Mat
        - b: Vec whose domain equals the column-label set of Q.
    Output:
        - The coordinate representation of b in terms of the rows of Q.
    Example:
        >>> Q = Mat(({0, 1}, {0, 1}), {(0, 1): 0, (1, 0): 0, (0, 0): 2, (1, 1): 2})
        >>> b = Vec({0, 1},{0: 4, 1: 2})
        >>> orthogonal_vec2rep(Q, b) == Vec({0, 1},{0: 8, 1: 4})
        True
    '''
    return Q * b



## Problem 4
def orthogonal_change_of_basis(A, B, a):
    '''
    Input:
        - A: an orthogonal Mat
        - B: an orthogonal Mat whose column labels are the row labels of A
        - a: the coordinate representation in terms of rows of A of some vector v 
    Output:
        - the Vec b such that b is the coordinate representation of v in terms of columns of B
    Example:
        >>> A = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): 0, (1, 2): 0, (0, 0): 1, (2, 0): 0, (1, 0): 0, (2, 2): 1, (0, 2): 0, (2, 1): 0, (1, 1): 1})
        >>> B = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): 0, (1, 2): 0, (0, 0): 2, (2, 0): 0, (1, 0): 0, (2, 2): 2, (0, 2): 0, (2, 1): 0, (1, 1): 2})
        >>> a = Vec({0, 1, 2},{0: 4, 1: 1, 2: 3})
        >>> orthogonal_change_of_basis(A, B, a) == Vec({0, 1, 2},{0: 8, 1: 2, 2: 6})
        True
    '''
    return (a * A) * B



## Problem 5
def orthonormal_projection_orthogonal(W, b):
    '''
    Input:
        - W: Mat whose rows are orthonormal
        - b: Vec whose labels are equal to W's column labels
    Output:
        - The projection of b orthogonal to W's row space.
    Example: 
        >>> W = Mat(({0, 1}, {0, 1, 2}), {(0, 1): 0, (1, 2): 0, (0, 0): 1, (1, 0): 0, (0, 2): 0, (1, 1): 1})
        >>> b = Vec({0, 1, 2},{0: 3, 1: 1, 2: 4})
        >>> orthonormal_projection_orthogonal(W, b) == Vec({0, 1, 2},{0: 0, 1: 0, 2: 4})
        True
    '''
    return project_orthogonal(b,mat2rowdict(W).values())



## Problem 6
# Write your solution for this problem in orthonormalization.py.



## Problem 7
# Write your solution for this problem in orthonormalization.py.



## Problem 8
# Please give each solution as a Vec

least_squares_A1 = listlist2mat([[8, 1], [6, 2], [0, 6]])
least_squares_Q1 = listlist2mat([[.8,-0.099],[.6, 0.132],[0,0.986]])
least_squares_R1 = listlist2mat([[10,2],[0,6.08]]) 
least_squares_b1 = list2vec([10, 8, 6])

x_hat_1 = Vec({0, 1},{0: 1.0832236842105263, 1: 0.9838815789473685})


least_squares_A2 = listlist2mat([[3, 1], [4, 1], [5, 1]])
least_squares_Q2 = listlist2mat([[.424, .808],[.566, .115],[.707, -.577]])
least_squares_R2 = listlist2mat([[7.07, 1.7],[0,.346]])
least_squares_b2 = list2vec([10,13,15])

x_hat_2 = Vec({0, 1},{0: 2.5010988382075188, 1: 2.658959537572257})



## Problem 9
def QR_solve(A, b):
    '''
    Input:
        - A: a Mat
        - b: a Vec
    Output:
        - vector x that minimizes norm(b - A*x)
    Example:
        >>> domain = ({'a','b','c'},{'A','B'})
        >>> A = Mat(domain,{('a','A'):-1, ('a','B'):2,('b','A'):5, ('b','B'):3,('c','A'):1,('c','B'):-2})
        >>> Q, R = QR.factor(A)
        >>> b = Vec(domain[0], {'a': 1, 'b': -1})
        >>> x = QR_solve(A, b)
        >>> result = A.transpose()*(b-A*x)
        >>> result * result < 1E-10
        True
    '''
    Q, R = factor(A)
    c = transpose(Q) * b
    x_hat = solve(R, transpose(Q) * b)
    return x_hat

# from vecutil import *
# from orthonormalization import *
# import QR
# from mat import Mat,transpose
# from solver import solve
# from vec import Vec
# from math import sqrt
# import matutil
# from hw7 import *
# vlist =[list2vec(x) for x in [[2, 4, 3, 5, 0], [4, -2, -5, 4, 0], [-8, 14, 21, -2, 0], [-1, -4,-4, 0, 0], [-2, -18, -19, -6, 0], [5, -3, 1, -5, 2]]]
# print(basis(vlist))
# v = [2, 4, 3, 5, 0]
# v * v
# Q = Mat(({0, 1}, {0, 1}), {(0, 1): 0, (1, 0): 0, (0, 0): 2, (1, 1): 2})
# b = Vec({0, 1},{0: 4, 1: 2})
# orthogonal_vec2rep(Q, b) == Vec({0, 1},{0: 8, 1: 4})
# A = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): 0, (1, 2): 0, (0, 0): 1, (2, 0): 0, (1, 0): 0, (2, 2): 1, (0, 2): 0, (2, 1): 0, (1, 1): 1})
# B = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): 0, (1, 2): 0, (0, 0): 2, (2, 0): 0, (1, 0): 0, (2, 2): 2, (0, 2): 0, (2, 1): 0, (1, 1): 2})
# a = Vec({0, 1, 2},{0: 4, 1: 1, 2: 3})
# orthogonal_change_of_basis(A, B, a) == Vec({0, 1, 2},{0: 8, 1: 2, 2: 6})
# A2 = matutil.listlist2mat([[1/sqrt(2), 1/sqrt(2), 0], [1/sqrt(3), -1/sqrt(3), 1/sqrt(3)], [-1/sqrt(6), 1/sqrt(6), 2/sqrt(6)]])
# B2 = matutil.listlist2mat([[1/sqrt(2), 1/sqrt(2), 0], [1/sqrt(3), -1/sqrt(3), 1/sqrt(3)], [-1/sqrt(6), 1/sqrt(6), 2/sqrt(6)]])
# a2 = Vec({0, 1, 2}, {0: sqrt(2), 1: 1/sqrt(3), 2: 2/sqrt(6)})
# orthogonal_change_of_basis(A2, B2, a2)
# W = Mat(({0, 1}, {0, 1, 2}), {(0, 1): 0, (1, 2): 0, (0, 0): 1, (1, 0): 0, (0, 2): 0, (1, 1): 1})
# b = Vec({0, 1, 2},{0: 3, 1: 1, 2: 4})
# orthonormal_projection_orthogonal(W, b) == Vec({0, 1, 2},{0: 0, 1: 0, 2: 4})
# L = [list2vec(v) for v in [[4,3,1,2],[8,9,-5,-5],[10,1,-1,5]]]
# print(matutil.coldict2mat(L))
# Qlist, Rlist = aug_orthonormalize(L)
# print(matutil.coldict2mat(Qlist))
# print(matutil.coldict2mat(Rlist))
# # to solve prob 8, read lecture 8-8 early half
# B = list2vec([10,8,6])
# Q = matutil.listlist2mat([[0.8, -0.099],[0.6, 0.132],[0,0.986]])
# R = matutil.listlist2mat([[10,2],[0,6.08]])
# A = Q * R
# c = transpose(Q) * B
# x = solve(R, c)
# x
# B = list2vec([10,13,15])
# Q = matutil.listlist2mat([[.424, .808],[.566, .115],[.707, -.577]])
# R = matutil.listlist2mat([[7.07, 1.7],[0,.346]])
# A = Q * R
# c = transpose(Q) * B
# x = solve(R, c)
# x

# domain = ({'a','b','c'},{'A','B'})
# A = Mat(domain,{('a','A'):-1, ('a','B'):2,('b','A'):5, ('b','B'):3,('c','A'):1,('c','B'):-2})
# Q, R = QR.factor(A)
# b = Vec(domain[0], {'a': 1, 'b': -1})
# x = QR_solve(A, b)
# result = A.transpose()*(b-A*x)
# result * result < 1E-10