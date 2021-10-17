#!/usr/bin/python3
""" Contains Rectangle class v2 """

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

    def __str__(self):
        """ returns a string representation of the Rectangle """
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))

    def area(self):
        """ Returns area of rectangle """
        return self.__width * self.__height
