# Please fill out this stencil and submit using the provided submission script.





## Problem 1
def myFilter(L, num):
    return [ n for n in L if n%num != 0 ]



## Problem 2
def myLists(L):
    return [ list(range(1,n+1)) for n in L]



## Problem 3
def myFunctionComposition(f, g):
    return {k:g[f[k]] for k in f.keys()}


## Problem 4
# Please only enter your numerical solution.

complex_addition_a = (5+3j)
complex_addition_b = 1j
complex_addition_c = (-1+0.001j)
complex_addition_d = (0.001+9j)



## Problem 5
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0


## Problem 6
def mySum(L):
    sum = 0
    for num in L:
        sum += num
    return sum



## Problem 7
def myProduct(L):
    prod = 1
    for num in L:
        prod *= num
    return prod



## Problem 8
def myMin(L):
    min = L[0]
    for num in L:
        if num < min:
            min = num
    return min



## Problem 9
def myConcat(L):
    cOut = ""
    for s in L:
        cOut += s
    return cOut



## Problem 10
def myUnion(L):
    un = set()
    for s in L:
        un |= s
    return un

def main():
    print(myFilter([1,2,4,5,7], 2))
    print(myLists([1,2,4]))
    print(myFunctionComposition({0:'a', 1:'b'}, {'a':'apple', 'b':'banana'}))

if __name__ == "__main__":
    main()
