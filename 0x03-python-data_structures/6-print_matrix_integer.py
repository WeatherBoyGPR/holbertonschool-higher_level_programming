#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if x < len(matrix[y]) - 1:
                print("{} ".format(matrix[y][x]), end='')
            else:
                print("{}".format(matrix[y][x]))
