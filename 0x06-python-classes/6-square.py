#!/usr/bin/python3
"""1-square.py"""


class Square:
    """ Acts as a sqaure."""
    def __init__(self, size=0, position=(0, 0)):
        """ Initiliazes class

        Args:
            size (int): Size of created square
            position (tuple): position of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[1] < 0 or position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """Will get the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Will get the position"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[1], int) or not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[1] < 0 or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            for i in range(self.__size + self.__position[1]):
                if i >= self.__position[1]:
                    for ix in range(self.__size + self.__position[0]):
                        if ix >= self.__position[0]:
                            print("#", end='')
                        else:
                            print(" ", end='')
                print("")
        else:
            print("")
