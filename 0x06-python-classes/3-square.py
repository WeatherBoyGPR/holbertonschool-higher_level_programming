#!/usr/bin/python3
"""1-square.py"""


class Square:
    """ Acts as a sqaure."""
    def __init__(self, size=0):
        """ Initiliazes class

        Args:
            size (int): Size of created square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ calculates area of square. """
        return self.__size * self.__size
