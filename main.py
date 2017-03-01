from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

print("creating matrices a (4x4) and b (4x8)...")
a = []
b = []
add_edge(a, 5, 5, 9, 10, 1, 2)
add_edge(a, 9, 3, 4, 4, 8, 7)
add_edge(b, 8, 3, 7, 6, 2, 7)
add_edge(b, 9, 1, 7, 7, 0, 7)
add_edge(b, 6, 8, 7, 9, 8, 7)
add_edge(b, 2, 9, 7, 1, 10, 7)

print("printing matrix a...")
print_matrix(a)

print("printing matrix b...")
print_matrix(b)

print("printing identity matrix for matrix a...")
ident(a)

print("multiplying matrix a by matrix b...")
matrix_mult(a, b)
print("================================================")

print("printing matrix b...")
print_matrix(b)

print("multiplying matrix a by 5...")
scalar_mult(a, 5)
print("================================================")

print("printing matrix a...")
print_matrix(a)

matrix = []
add_edge(matrix, 2, 2, 0, 2, 123, 0)
add_edge(matrix, 2, 123, 0, 123, 123, 0)
add_edge(matrix, 123, 123, 0, 123, 2, 0)
add_edge(matrix, 123, 2, 0, 2, 2, 0)

draw_lines( matrix, screen, color )

while matrix[0][0] < 500:
    scalar_mult(matrix, 2)
    draw_lines(matrix, screen, color)

display(screen)
