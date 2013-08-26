from image_mat_util import *

from mat import Mat
from vec import Vec
import matutil

from solver import solve

## Task 1
def move2board(v): 
    '''
    Input:
        - v: a vector with domain {'y1','y2','y3'}, the coordinate representation of a point q.
    Output:
        - A {'y1','y2','y3'}-vector z, the coordinate representation
          in whiteboard coordinates of the point p such that the line through the 
          origin and q intersects the whiteboard plane at p.
    '''
    return Vec({'y1','y2','y3'}, { key:val/v.f['y3'] for key, val in v.f.items() })

## Task 2
def make_equations(x1, x2, w1, w2):
    '''
    Input:
        - x1 & x2: photo coordinates of a point on the board
        - y1 & y2: whiteboard coordinates of a point on the board
    Output:
        - List [u,v] where u*h = 0 and v*h = 0
    '''
    domain = {(a, b) for a in {'y1', 'y2', 'y3'} for b in {'x1', 'x2', 'x3'}}
    u = Vec(domain, {('y3','x1'):w1*x1,('y3','x2'):w1*x2,('y3','x3'):w1,('y1','x1'):-x1,('y1','x2'):-x2,('y1','x3'):-1})
    v = Vec(domain, {('y3','x1'):w2*x1,('y3','x2'):w2*x2,('y3','x3'):w2,('y2','x1'):-x1,('y2','x2'):-x2,('y2','x3'):-1})
    return [u, v]

## Task 3
H = Mat(({'y1', 'y3', 'y2'}, {'x2', 'x3', 'x1'}), {('y3', 'x1'): -0.7219356810710031, ('y2', 'x1'): -0.3815213180054361, ('y2', 'x2'): 0.7378180860600992, ('y1', 'x1'): 1.0, ('y2', 'x3'): 110.0231807477826, ('y3', 'x3'): 669.4762699006177, ('y1', 'x3'): -359.86096256684493, ('y3', 'x2'): -0.011690730864965311, ('y1', 'x2'): 0.05169340463458105})

## Task 4
def mat_move2board(Y):
    '''
    Input:
        - Y: Mat instance, each column of which is a 'y1', 'y2', 'y3' vector 
          giving the whiteboard coordinates of a point q.
    Output:
        - Mat instance, each column of which is the corresponding point in the
          whiteboard plane (the point of intersection with the whiteboard plane 
          of the line through the origin and q).
    '''
    col_dict = matutil.mat2coldict(Y)
    new_col_dic = {}

    for key, val in col_dict.items():
        new_col_dic[key] = Vec(val.D, { k:v/val.f['y3'] for k, v in val.f.items() })

    return matutil.coldict2mat(new_col_dic)

# import perspective_lab
# from mat import Mat
# import vecutil
# import matutil
# import image_mat_util
# from vec import Vec
# from GF2 import one
# from solver import solve
# row_dict = {}
# row_dict[0] = perspective_lab.make_equations(358, 36, 0, 0)[0]
# row_dict[1] = perspective_lab.make_equations(358, 36, 0, 0)[1]
# row_dict[2] = perspective_lab.make_equations(329, 597, 0, 1)[0]
# row_dict[3] = perspective_lab.make_equations(329, 597, 0, 1)[1]
# row_dict[4] = perspective_lab.make_equations(592, 157, 1, 0)[0]
# row_dict[5] = perspective_lab.make_equations(592, 157, 1, 0)[1]
# row_dict[6] = perspective_lab.make_equations(580, 483, 1, 1)[0]
# row_dict[7] = perspective_lab.make_equations(580, 483, 1, 1)[1]
# foo = perspective_lab.make_equations(0, 0, 0, 0)[0]
# foo[('y1', 'x1')] = 1
# foo[('y1', 'x3')] = 0
# row_dict[8] = foo
# M = matutil.rowdict2mat(row_dict)
# print(M)
# solve(M, vecutil.list2vec([0, 0, 0, 0, 0, 0, 0, 0, 1]))
# Y_in = Mat(({'y1', 'y2', 'y3'}, {0,1,2,3}),
#            {('y1',0):2, ('y2',0):4, ('y3',0):8,
#             ('y1',1):10, ('y2',1):5, ('y3',1):5,
#             ('y1',2):4, ('y2',2):25, ('y3',2):2,
#             ('y1',3):5, ('y2',3):10, ('y3',3):4})
# print(Y_in)
# print(perspective_lab.mat_move2board(Y_in))
# (X_pts, colors) = image_mat_util.file2mat('board.png', ('x1','x2','x3'))
# H = Mat(({'y1', 'y3', 'y2'}, {'x2', 'x3', 'x1'}), {('y3', 'x1'): -0.7219356810710031, ('y2', 'x1'): -0.3815213180054361, ('y2', 'x2'): 0.7378180860600992, ('y1', 'x1'): 1.0, ('y2', 'x3'): 110.0231807477826, ('y3', 'x3'): 669.4762699006177, ('y1', 'x3'): -359.86096256684493, ('y3', 'x2'): -0.011690730864965311, ('y1', 'x2'): 0.05169340463458105})
# Y_pts = H * X_pts
# Y_board = perspective_lab.mat_move2board(Y_pts)
# image_mat_util.mat2display(Y_board, colors, ('y1', 'y2', 'y3'),
#                            scale=100, xmin=None, ymin=None)