#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix:
        return ([list(map(lambda x: x * x, row)) for row in matrix])
