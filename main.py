from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()
b = [[1, 1, 1, 1],
     [1, 1, 1, 1],
     [1, 1, 1, 1],
     [1, 1, 1, 1]]

a = [[2, 2, 2, 2],
     [2, 2, 2, 2],
     [2, 2, 2, 2],
     [2, 2, 2, 2]]

print_matrix(b)
matrix_mult(a, b)
print("--------------------------------------------------------")
print_matrix(b)

draw_lines( matrix, screen, color )
display(screen)
