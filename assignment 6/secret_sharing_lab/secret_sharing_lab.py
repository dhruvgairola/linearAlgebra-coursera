# version code 988
# Please fill out this stencil and submit using the provided submission script.

import random
from GF2 import one
from vecutil import list2vec
from vec import Vec
import independence

## Problem 1
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])
a1 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: one, 3: one, 4: 0, 5: one})
b1 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: 0, 3: one, 4: one, 5: 0})
a2 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: one, 3: 0, 4: one, 5: one})
b2 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: one, 2: 0, 3: 0, 4: one, 5: 0})
a3 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: 0, 3: 0, 4: one, 5: 0})
b3 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: one, 2: 0, 3: one, 4: one, 5: one})
a4 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: one, 3: 0, 4: 0, 5: 0})
b4 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: one, 2: one, 3: one, 4: 0, 5: one})

def choose_secret_vector(s,t):
    set = False
    while not set:
        secret_vector = generateSecretVector(a0.D)
        if a0 *  secret_vector == s and b0 * secret_vector == t:
            set = True
            return secret_vector
        else:
            continue

def generateSecretVector(D):
    secretVector = Vec(D, {})
    for d in D:
        secretVector[d] = randGF2()
    return secretVector

def randGF2(): return random.randint(0,1)*one

cache = []

def sel_all_vecs():
    '''
    Algo:
    1. Start with a0,b0, grow a1,b1,a2,b2 randomly so they are linearly independent.
    2. Keep generating random a3,b3 until any 3 pairs of vecs are linearly independent.
    3. Keep generating random a4,b4 until any 3 pairs of vecs are linearly independent.
    '''
    selected = False

    while not selected:
        fivePairs = []
        fivePairs.append((a0, b0))
        fivePairs.append((a1, b1))
        fivePairs.append((a2, b2))
        fivePairs.append((a3, b3))
        fivePairs.append((generateSecretVector(a0.D), generateSecretVector(a0.D)))

        threePairsList = generateAllThreePairsList(fivePairs)
        passed = False

        # Look at the printed value of Threes and modify the list below
        # based on this
        t0 = threePairsList[0]
        t1 = threePairsList[1]
        t2 = threePairsList[2]
        t3 = threePairsList[3]
        t4 = threePairsList[4]
        t5 = threePairsList[5]
        t6 = threePairsList[6]
        t7 = threePairsList[7]
        t8 = threePairsList[8]
        t9 = threePairsList[9]
        r1 = independence.rank(t0[0]+t0[1]+t0[2])
        r2 = independence.rank(t1[0]+t1[1]+t1[2])
        r3 = independence.rank(t2[0]+t2[1]+t2[2])
        r4 = independence.rank(t3[0]+t3[1]+t3[2])
        r5 = independence.rank(t4[0]+t4[1]+t4[2])
        r6 = independence.rank(t5[0]+t5[1]+t5[2])
        r7 = independence.rank(t6[0]+t6[1]+t6[2])
        r8 = independence.rank(t7[0]+t7[1]+t7[2])
        r9 = independence.rank(t8[0]+t8[1]+t8[2])
        r10 = independence.rank(t9[0]+t9[1]+t9[2])

        if r1 == r2 ==r3 == r4==r5==r6==r7==r8==r9==r10 and r1 == 6:
            print(t0)
            print(t1)
            print(t2)


def generateAllThreePairsList(fivePairs):
    threePairsList = []
    fivePairsLab = {}
    subsets = generateSubsets([0, 1, 2, 3, 4], 0)
    threes = []

    for s in subsets:
        if len(s) == 3 and filters(s):
            threes.append(s)

    print("threes: ",threes)
    for i,pair in enumerate(fivePairs):
        fivePairsLab[i] = pair

    for t in threes:
        f0 = fivePairsLab[t[0]]
        f1 = fivePairsLab[t[1]]
        f2 = fivePairsLab[t[2]]

        threePairsList.append([(f0[0], f0[1]), (f1[0], f1[1]), (f2[0], f2[1])])

    return threePairsList

def filters(s):
    '''
    modify this
    '''
    # return ((0 in s and 1 in s) or (0 in s and 2 in s) or (2 in s and 1 in s)) and 4 in s
    return True

def generateSubsets(set, index):
    allSubsets = None

    if index == len(set):
        allSubsets = [[]]
    else:
        allSubsets = generateSubsets(set, index+1)
        first_element = set[index]
        new_subsets = []
        for sub in allSubsets:
            new_s = []
            new_s += sub
            new_s.append(first_element)
            new_subsets.append(new_s)

        allSubsets += new_subsets

    return allSubsets


## Problem 2
# Give each vector as a Vec instance
secret_a0 = list2vec([one, one,   0, one,   0, one])
secret_b0 = list2vec([one, one,   0,   0,   0, one])
secret_a1 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: one, 3: one, 4: 0, 5: one})
secret_b1 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: 0, 3: one, 4: one, 5: 0})
secret_a2 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: one, 3: 0, 4: one, 5: one})
secret_b2 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: one, 2: 0, 3: 0, 4: one, 5: 0})
secret_a3 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: 0, 3: 0, 4: one, 5: 0})
secret_b3 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: one, 2: 0, 3: one, 4: one, 5: one})
secret_a4 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: one, 3: 0, 4: 0, 5: 0})
secret_b4 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: one, 2: one, 3: one, 4: 0, 5: one})