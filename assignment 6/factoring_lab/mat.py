from vec import Vec

def getitem(M, k):
    "Returns the value of entry k in M.  The value of k should be a pair."
    assert k[0] in M.D[0] and k[1] in M.D[1]

    if (k[0], k[1]) in M.f.keys():
        return M.f[(k[0], k[1])]
    else:
        return 0

def setitem(M, k, val):
    "Sets the element of v with label k to be val.  The value of k should be a pair"
    assert k[0] in M.D[0] and k[1] in M.D[1]

    M.f[(k[0], k[1])] = val

def add(A, B):
    "Returns the sum of A and B"
    assert A.D == B.D

    added_matrix = Mat(A.D, {})

    for key, val in A.f.items():
        added_matrix.f[key] = val

    for key, val in B.f.items():
        if key in added_matrix.f.keys():
            added_matrix.f[key] += val
        else:
            added_matrix.f[key] = val

    return added_matrix

def scalar_mul(M, alpha):
    "Returns the product of scalar alpha with M"
    return Mat(M.D, {key: (val * alpha) for key, val in M.f.items()})

def equal(A, B):
    "Returns true iff A is equal to B"
    assert A.D == B.D

    for r in A.D[0]:
        for c in A.D[1]:
            if (r, c) not in A.f.keys():
                A.f[(r, c)] = 0

    for r in B.D[0]:
        for c in B.D[1]:
            if (r, c) not in B.f.keys():
                B.f[(r, c)] = 0

    return A.f == B.f


def transpose(M):
    "Returns the transpose of M"
    return Mat((M.D[1], M.D[0]), { (q, p):v for (p, q), v in M.f.items() })

def vector_matrix_mul(v, M):
    "Returns the product of vector v and matrix M"
    assert M.D[0] == v.D

    ret_v = Vec(M.D[1], {})

    for d in ret_v.D:
        ret_v.f[d] = 0

    for (k1, k2), val in M.f.items():
        ret_v.f[k2] += val * v[k1]

    return ret_v

def matrix_vector_mul(M, v):
    "Returns the product of matrix M and vector v"
    assert M.D[1] == v.D

    ret_v = Vec(M.D[0], {})

    for d in ret_v.D:
        ret_v.f[d] = 0

    for (k1, k2), val in M.f.items():
        ret_v.f[k1] += val * v[k2]

    return ret_v

def matrix_matrix_mul(A, B):
    "Returns the product of A and B"
    from matutil import mat2coldict, mat2rowdict

    assert A.D[1] == B.D[0]
    ret_mat = Mat((A.D[0], B.D[1]), {})

    a_row = mat2rowdict(A)
    b_col = mat2coldict(B)

    for key, val in a_row.items():
        for key2, val2 in b_col.items():
            ret_mat.f[(key, key2)] = val * val2

    return ret_mat

################################################################################

class Mat:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function

    __getitem__ = getitem
    __setitem__ = setitem
    transpose = transpose

    def __neg__(self):
        return (-1)*self

    def __mul__(self,other):
        if Mat == type(other):
            return matrix_matrix_mul(self,other)
        elif Vec == type(other):
            return matrix_vector_mul(self,other)
        else:
            return scalar_mul(self,other)
            #this will only be used if other is scalar (or not-supported). mat and vec both have __mul__ implemented

    def __rmul__(self, other):
        if Vec == type(other):
            return vector_matrix_mul(other, self)
        else:  # Assume scalar
            return scalar_mul(self, other)

    __add__ = add

    def __sub__(a,b):
        return a+(-b)

    __eq__ = equal

    def copy(self):
        return Mat(self.D, self.f.copy())

    def __str__(M, rows=None, cols=None):
        "string representation for print()"
        if rows == None:
            try:
                rows = sorted(M.D[0])
            except TypeError:
                rows = sorted(M.D[0], key=hash)
        if cols == None:
            try:
                cols = sorted(M.D[1])
            except TypeError:
                cols = sorted(M.D[1], key=hash)
        separator = ' | '
        numdec = 3
        pre = 1+max([len(str(r)) for r in rows])
        colw = {col:(1+max([len(str(col))] + [len('{0:.{1}G}'.format(M[row,col],numdec)) if isinstance(M[row,col], int) or isinstance(M[row,col], float) else len(str(M[row,col])) for row in rows])) for col in cols}
        s1 = ' '*(1+ pre + len(separator))
        s2 = ''.join(['{0:>{1}}'.format(c,colw[c]) for c in cols])
        s3 = ' '*(pre+len(separator)) + '-'*(sum(list(colw.values())) + 1)
        s4 = ''.join(['{0:>{1}} {2}'.format(r, pre,separator)+''.join(['{0:>{1}.{2}G}'.format(M[r,c],colw[c],numdec) if isinstance(M[r,c], int) or isinstance(M[r,c], float) else '{0:>{1}}'.format(M[r,c], colw[c]) for c in cols])+'\n' for r in rows])
        return '\n' + s1 + s2 + '\n' + s3 + '\n' + s4

    def pp(self, rows, cols):
        print(self.__str__(rows, cols))

    def __repr__(self):
        "evaluatable representation"
        return "Mat(" + str(self.D) +", " + str(self.f) + ")"
