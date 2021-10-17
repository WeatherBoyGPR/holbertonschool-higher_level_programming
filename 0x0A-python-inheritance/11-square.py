#!/usr/bin/python3
""" Contains Square class """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square: acts as a square
    Args:
        size (int): size of square
    """

    def __init__(self, size):
        """ __init__
        Args:
            size (int): size of square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """ Returns string representing square """
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
