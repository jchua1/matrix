import math


def print_matrix( matrix ):
    for i in range(0, len(matrix)):
        print matrix[i]
    pass

def ident( matrix ):
    pass

def scalar_mult( matrix, s ):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            matrix[i][j] *= s
    pass

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    temp = []
    for i in 
    pass




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
