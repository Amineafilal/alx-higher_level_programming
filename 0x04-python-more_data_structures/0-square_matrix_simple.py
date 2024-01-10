#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_square = list(map(lambda a: list(map(lambda b: b*b, a)), matrix))
    return (matrix_square)
