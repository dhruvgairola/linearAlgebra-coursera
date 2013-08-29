from vec import Vec
from GF2 import one

from factoring_support import dumb_factor
from factoring_support import intsqrt
from factoring_support import gcd
from factoring_support import primes
from factoring_support import prod

import echelon

## Task 1
def int2GF2(i):
    '''
    Returns one if i is odd, 0 otherwise.

    Input:
        - i: an int
    Output:
        - one if i is congruent to 1 mod 2
        - 0   if i is congruent to 0 mod 2
    Examples:
        >>> int2GF2(3)
        one
        >>> int2GF2(100)
        0
    '''
    return one if i % 2 == 1 else 0

## Task 2
def make_Vec(primeset, factors):
    '''
    Input:
        - primeset: a set of primes
        - factors: a list of factors [(p_1,a_1), ..., (p_n, a_n)]
                   with p_i in primeset
    Output:
        - a vector v over GF(2) with domain primeset
          such that v[p_i] = int2GF2(a_i) for all i
    Example:
        >>> make_Vec({2,3,11}, [(2,3), (3,2)]) == Vec({2,3,11},{2:one})
        True
    '''
    return Vec(primeset, {i:int2GF2(j) for (i, j) in factors})

## Task 3
def find_candidates(N, primeset):
    '''
    Input:
        - N: an int to factor
        - primeset: a set of primes

    Output:
        - a list [roots, rowlist]
        - roots: a list a_0, a_1, ..., a_n where a_i*a_i - N can be factored
                 over primeset
        - rowlist: a list such that rowlist[i] is a
                   primeset-vector over GF(2) corresponding to a_i
          such that len(roots) = len(rowlist) and len(roots) > len(primeset)
    '''
    roots = []
    rowlist = []
    increment = 2

    while len(roots) < len(primeset) + 1:
        x = intsqrt(N) + increment
        increment += 1
        xx_minus_n = x ** 2 - N
        factors = dumb_factor(xx_minus_n, primeset)
        if factors:
            roots.append(x)
            rowlist.append(make_Vec(primeset, factors))

    return (roots, rowlist)



## Task 4
def find_a_and_b(v, roots, N):
    '''
    Input: 
     - a {0,1,..., n-1}-vector v over GF(2) where n = len(roots)
     - a list roots of integers
     - an integer N to factor
    Output:
      a pair (a,b) of integers
      such that a*a-b*b is a multiple of N
      (if v is correctly chosen)
    '''
    alist = [roots[key] for key, val in v.f.items() if val != 0]
    a = prod(alist)
    c = prod([x*x - N for x in alist])
    b = intsqrt(c)
    assert b*b == c
    return (a, b)

def gcd(x,y): return x if y == 0 else gcd(y, x % y)

## Task 5

smallest_nontrivial_divisor_of_2461799993978700679 = 1230926561


# import factoring_lab
# from GF2 import one
# from factoring_lab import find_a_and_b, find_candidates, gcd
# from vec import Vec
# from factoring_support import dumb_factor
# from factoring_support import intsqrt
# from factoring_support import gcd
# from factoring_support import primes
# from factoring_support import prod
# find_candidates(2419, {2,3,5,7,11,13,17,19,23,29,31})
# v = Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11},{0: 0, 1: one, 2: one, 4: 0, 5: one, 11: one})
# N = 2419
# roots = [51, 52, 53, 58, 61, 62, 63, 67, 68, 71, 77, 79]
# print(find_a_and_b(v, roots, N))
# AssertionError
# v = Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11},{0: 0, 1: 0, 10: one, 2: one})
# N = 2419
# roots = [51, 52, 53, 58, 61, 62, 63, 67, 68, 71, 77, 79]
# print(find_a_and_b(v, roots, N))
