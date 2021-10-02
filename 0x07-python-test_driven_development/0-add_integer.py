#!/usr/bin/python3
"""Holds add integer function"""
def add_integer(a, b=98):
    """ Will add two numbers.
    Args:
        a (int) or (float): First integer to add
        b (int) or (float): Second integer to add
    Return:
        sum of a and b in integer form
    """
    op1 = a
    op2 = b
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        op1 = int(a)
    if isinstance(b, float):
        op2 = int(b)
    return (op1 + op2)
