from mat import *
from vec import Vec
from cancer_data import *

## Task 1 ##
def signum(u):
    '''
    Input:
        - u: Vec
    Output:
        - v: Vec such that:
            if u[d] >= 0, then v[d] =  1
            if u[d] <  0, then v[d] = -1
    Example:
        >>> signum(Vec({1,2,3},{1:2, 2:-1})) == Vec({1,2,3},{1:1,2:-1,3:1})
        True
    '''
    return Vec(u.D, {key: 1 if key not in u.f or u.f[key] >= 0 else -1 for key in u.D})

## Task 2 ##
def fraction_wrong(A, b, w):
    '''
    Input:
        - A: a Mat with rows as feature vectors
        - b: a Vec of actual diagnoses
        - w: hypothesis Vec
    Output:
        - Fraction (as a decimal in [0,1]) of vectors incorrectly
          classified by w 
    '''
    v = signum(A * w) - b
    wrong_count = 0

    for key, val in v.f.items():
        if val != 0:
            wrong_count += 1

    return wrong_count / len(v.D)

## Task 3 ##
def loss(A, b, w):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
    Output:
        - Value of loss function at w for training data
    '''
    v = (A * w) - b

    loss_val = 0

    for key, val in v.f.items():
        loss_val += val * val

    return loss_val

## Task 4 ##
def find_grad(A, b, w):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
    Output:
        - Value of the gradient function at w
    '''
    grad = 2 * ((A * w) - b) * A
    return grad

## Task 5 ##
def gradient_descent_step(A, b, w, sigma):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
        - sigma: step size
    Output:
        - The vector w' resulting from 1 iteration of gradient descent
          starting from w and moving sigma.
    '''
    return w - sigma * find_grad(A, b, w)


def gradient_descent(A, b, w, sigma, T):

    for t in range(T):
        new_w = gradient_descent_step(A, b, w, sigma)
        w = new_w

    return w

# import matutil
# import vecutil
# from machine_learning_lab import *
# from vec import Vec
# from cancer_data import *
# data = read_training_data("train.data")
# signum(Vec({1,2,3},{1:2, 2:-1})) == Vec({1,2,3},{1:1,2:-1,3:1})
# w = vecutil.list2vec([1,1,1])
# b = vecutil.list2vec([1,1,-1])
# A = matutil.listlist2mat([[10,20,-30],[50,-60,80], [2,4,5]])
# fraction_wrong(A, b, w)
# loss(A, b, w)
# find_grad(A, b, w)