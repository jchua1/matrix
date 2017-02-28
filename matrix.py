import math


def print_matrix( matrix ):
    for r in range(0, len(matrix)):
        row = ""
        for c in range(0, len(matrix[r])):
            row += str(matrix[r][c]) + " "
        print row + "\n"
    pass

def ident( matrix ):
    identity = []
    for i in range(0, len(matrix)):
        row = [0] * len(matrix)
        identity.append(row)
    for i in range(0, len(identity)):
        identity[i][i] = 1
    print_matrix(identity)
    pass

def scalar_mult( matrix, s ):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            matrix[i][j] *= s
    pass

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    temp = []

    for r in range(0, 4):
        row = [0] * len(m2[0])
        for c2 in range(0, len(m2[0])):
            for c1 in range(0, 4):
                row[c2] += m1[r][c1] * m2[c1][c2]
        temp.append(row)

    for tr in range(len(m2)):
        for tc in range(len(m2[tr])):
            m2[tr][tc] = temp [tr][tc]
    pass




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
