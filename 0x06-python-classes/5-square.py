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

    @property
    def size(self):
        """ Will get the size. """
        return self.__size

    @size.setter
    def size(self, value):
        """ Will set the size. """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculates area of square. """
        return self.__size * self.__size

    def my_print(self):
        """ Prints the square. """
        if self.__size > 0:
            for i in range(self.__size):
                for i in range(self.__size):
                    print("#", end='')
                print("")
        else:
            print("")
