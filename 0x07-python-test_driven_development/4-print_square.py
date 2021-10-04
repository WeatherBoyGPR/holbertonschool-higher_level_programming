#!/usr/bin/python3
""" Module for holding function print_square. """


def print_square(size):
    """ print_square
    Will print a square using hash symbols
    Args:
        size (int): size of square to print
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for y in range(size):
        print("#" * size)
