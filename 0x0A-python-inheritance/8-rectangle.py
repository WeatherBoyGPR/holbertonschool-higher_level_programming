#!/usr/bin/python3
""" Contains Rectangle class """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class that represents aspects of a rectangle """

    def __init__(self, width, height):
        """ __init__
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
