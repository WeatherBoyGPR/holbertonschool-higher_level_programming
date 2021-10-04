#!/usr/bin/python3
"""2.matrix_divided.py: holds function for task 1"""


def matrix_divided(matrix, div):
    """ Will divide every element of a matrix
    Args:
        matrix (list of list of (integers) or (floats): matrix to be processed
        div (int) or (float): non-zero number to divide matrix by
    Return:
        new matrix with dividends of elements and div
    """
    warning = "matrix must be a matrix (list of lists) "

    if not isinstance(matrix, list):
        raise TypeError(warning + "of integers/floats")
    y = len(matrix[0])
    res = []
    wa
    if div is 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    for x in matrix:
        if not isinstance(x, list):
            raise TypeError(warning + "of integers/floats")
        if len(x) != y:
            raise TypeError("Each row of the matrix must have the same size")
        new = []
        for num in x:
            if type(num) is not int and type(num) is not float:
                raise TypeError(warning + "of integers/floats")
            new.append(round(num / div, 2))
        res.append(new)
    return res
