from mat import Mat
import math

## Task 1
def identity(labels = {'x','y','u'}):
    '''
    In case you have never seen this notation for a parameter before,
    the way it works is that identity() now defaults to having labels 
    equal to {'x','y','u'}.  So you should write your procedure as if 
    it were defined 'def identity(labels):'.  However, if you want the labels of 
    your identity matrix to be {'x','y','u'}, you can just call 
    identity().  Additionally, if you want {'r','g','b'}, or another set, to be the
    labels of your matrix, you can call identity({'r','g','b'}).  
    '''
    return Mat((labels, labels), { (l, l2): 1 for l in labels for l2 in labels if l == l2})

## Task 2
def translation(x,y):
    '''
    Input:  An x and y value by which to translate an image.
    Output:  Corresponding 3x3 translation matrix.
    '''
    f = {}
    f[('x', 'x')] = 1
    f[('x', 'u')] = x
    f[('y', 'y')] = 1
    f[('y', 'u')] = y
    f[('u', 'u')] = 1

    return Mat(({'x', 'y', 'u'}, {'x', 'y', 'u'}), f)

## Task 3
def scale(a, b):
    '''
    Input:  Scaling parameters for the x and y direction.
    Output:  Corresponding 3x3 scaling matrix.
    '''
    f = {}
    f[('x', 'x')] = a
    f[('y', 'y')] = b
    f[('u', 'u')] = 1

    return Mat(({'x', 'y', 'u'}, {'x', 'y', 'u'}), f)

## Task 4
def rotation(angle):
    '''
    Input:  An angle in radians to rotate an image.
    Output:  Corresponding 3x3 rotation matrix.
    Note that the math module is imported.
    '''
    f = {}
    f[('x', 'x')] = math.cos(angle)
    f[('x', 'y')] = -1 * math.sin(angle)
    f[('y', 'x')] = math.sin(angle)
    f[('y', 'y')] = math.cos(angle)
    f[('u', 'u')] = 1

    return Mat(({'x', 'y', 'u'}, {'x', 'y', 'u'}), f)

## Task 5
def rotate_about(x,y,angle):
    '''
    Input:  An x and y coordinate to rotate about, and an angle
    in radians to rotate about.
    Output:  Corresponding 3x3 rotation matrix.
    It might be helpful to use procedures you already wrote.
    '''
    mat1 = translation(-x, -y)
    mat2 = rotation(angle)
    mat3 = translation(x, y)
    return mat3 * mat2 * mat1

## Task 6
def reflect_y():
    '''
    Input:  None.
    Output:  3x3 Y-reflection matrix.
    '''
    return scale(-1, 1)

## Task 7
def reflect_x():
    '''
    Inpute:  None.
    Output:  3x3 X-reflection matrix.
    '''
    return scale(1, -1)
    
## Task 8    
def scale_color(scale_r,scale_g,scale_b):
    '''
    Input:  3 scaling parameters for the colors of the image.
    Output:  Corresponding 3x3 color scaling matrix.
    '''
    f = {}
    f[('r', 'r')] = scale_r
    f[('g', 'g')] = scale_g
    f[('b', 'b')] = scale_b

    return Mat(({'r', 'g', 'b'}, {'r', 'g', 'b'}), f)

## Task 9
def grayscale():
    '''
    Input: None
    Output: 3x3 greyscale matrix.
    '''
    f = {}
    f[('r', 'r')] = 77/256
    f[('r', 'g')] = 151/256
    f[('r', 'b')] = 28/256
    f[('g', 'r')] = 77/256
    f[('g', 'g')] = 151/256
    f[('g', 'b')] = 28/256
    f[('b', 'r')] = 77/256
    f[('b', 'g')] = 151/256
    f[('b', 'b')] = 28/256

    return Mat(({'r', 'g', 'b'}, {'r', 'g', 'b'}), f)

## Task 10
def reflect_about(p1,p2):
    '''
    Input: 2 points that define a line to reflect about.
    Output:  Corresponding 3x3 reflect about matrix.
    '''
    x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
    theta = math.atan2(y2 - y1, x2 - x1)
    return translation(x2,y2)*rotation(theta)*reflect_x()*rotation(-theta)*translation(-x2,-y2)


# input into python3 REPL:
# import image
# import image_mat_util
# import geometry_lab
# cit = image_mat_util.file2mat("/Users/dhruvgairola/Documents/Courses/Coding the Matrix- Lin Algebra, Brown/matrix/geometry_lab/cit.png")
# I = geometry_lab.identity({'r','b','g'})
# T = geometry_lab.translation(3,2)
# Ra = geometry_lab.rotate_about(3,2, 0.2)
# cit = cit * geometry_lab.grayscale()
# image_mat_util.mat2display(cit[0], cit[1])
# image_mat_util.mat2display(cit[0], geometry_lab.grayscale() * cit[1])


