import sys

def hw():
    # min = 24 * 7 * 60
    # print(min)
    # remainder = 2304811 - (2304811 // 47) * 47
    # print(remainder)
    # is_div_3 = (909 + 673) % 3 == 0
    # print(is_div_3)
    # x = -9
    # y = 1/2
    # statement_val = 2**(y+1/2) if x+10<0 else 2**(y-1/2)
    # print(statement_val)
    # first_five_squares = { x**2 for x in {1,2,3,4,5} }
    # print(first_five_squares)
    # first_five_pows_two = { 2**x for x in {0,1,2,3,4} }
    # print(first_five_pows_two)
    # X1 = { 1, 2, 3 }
    # Y1 = { 4, 7, 11 }
    # print({ x*y for x in X1 for y in Y1})
    # X2 = { 1, -2, 4 }
    # Y2 = { 0, -4, 2 }
    # print({ x*y for x in X2 for y in Y2 if x != y})
    # base = 10
    # digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    # three_digits_set = { (base ** 2) * x + base * y + z for x in digits for y in digits for z in digits if (base ** 2) * x + base * y + z < 1000 }
    # print(three_digits_set)
    # S = {1, 2, 3, 4}
    # T = {3, 4, 5, 6}
    # print({ x for x in S for y in T if x == y})
    # L_average = sum([20, 10, 15, 75]) / len([20, 10, 15, 75])
    # print(L_average)
    # LofL = [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
    # LofL_sum = sum([sum(x) for x in LofL ])
    # print(LofL_sum)
    # cartesian_product = [ [x, y] for x in {'A', 'B', 'C'} for y in {1,2,3}]
    # print(cartesian_product)
    # S = {-4, -2, 1, 2, 5, 0}
    # zero_sum_list = [ (x, y, z) for x in S for y in S for z in S if x + y + z == 0 ]
    # print(zero_sum_list)
    # exclude_zero_list = [ (x, y, z) for x in S for y in S for z in S if x + y + z == 0 and not (x == 0 and y == 0 and z == 0) ]
    # print(exclude_zero_list)
    # first_of_tuples_list = [ (x, y, z) for x in S for y in S for z in S if x + y + z == 0 and not (x == 0 and y == 0 and z == 0) ][0]
    # print(first_of_tuples_list)
    # L1 = [1,2,3,3] # <-- want len(L1) != len(list(set(L1)))
    # print(len(L1) != len(list(set(L1))))
    # L2 = [2,1,3] # <-- same len(L2) == len(list(set(L2))) but L2 != list(set(L2))
    # print(len(L2) == len(list(set(L2))) and L2 != list(set(L2)))
    # odd_num_list_range = {x for x in range(1, 100) if x % 2 == 1}
    # print(odd_num_list_range)
    # L = ['A','B','C','D','E']
    # range_and_zip = list(zip(list(range(5)), L))
    # print(range_and_zip)
    # list_sum_zip = [ x + y for (x, y) in zip([10, 25, 40], [1, 15, 20])]
    # print(list_sum_zip)
    # dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]
    # k = 'James'
    # value_list = [x[k] for x in dlist]
    # print(value_list)
    # dlist = [{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Richard'}]
    # k = 'Bilbo'
    # value_list_modified_1 = [x[k] if k in x else 'NOT PRESENT' for x in dlist] # <-- Use the same expression here
    # print(value_list_modified_1)
    # k = 'Frodo'
    # value_list_modified_2 = [x[k] if k in x else 'NOT PRESENT' for x in dlist] # <-- as you do here
    # print(value_list_modified_2)
    # square_dict = { x:x**2 for x in range(100) }
    # print(square_dict)
    # D = {'red','white','blue'}
    # identity_dict = {x:x for x in D}
    # print(identity_dict)
    # base = 10
    # digits = set(range(10))
    # representation_dict = {(base ** 2) * x + base * y + z:[x , y , z] for x in digits for y in digits for z in digits}
    # print(representation_dict)
    # d = {0:1000.0, 3:1200.50, 2:990}
    # names = ['Larry', 'Curly', '', 'Moe']
    # listdict2dict = {names[i]:d[i] if i in d else 0.0 for i in range(len(names))}
    # print(listdict2dict)
    # print(nextInts([1, 5, 7]))
    # print(cubes([1, 5, 7]))
    # print(dict2list({'a':'A', 'b':'B', 'c':'C'}, ['b','c','a']))
    print(list2dict(['A','B','C'], ['a','b','c']))

def nextInts(L):
    return [x + 1 for x in L]

def cubes(L):
    return [x**3 for x in L]

def dict2list(dct, keylist):
    return [ dct[x] for x in keylist ]

def list2dict(L, keylist):
    return { k:v for (k,v) in zip(keylist, L) }

def main():
    hw()

if __name__ == "__main__":
    main()
