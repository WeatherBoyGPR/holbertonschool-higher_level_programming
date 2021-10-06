#!/usr/bin/python3
""" Module that contains Rectangle Class. """


class Rectangle:
    """ Acts as a Rectangle."""
    def __init__(self, width=0, height=0):
        """ __init__
        initializes class
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Retrieves private width attribute. """
        return self.__width

    @width.setter
    def width(self, value):
        """ width
        Sets width of rectangle
        Args:
            value (int): width of rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Retrieves private height attribute. """
        return self.__height

    @height.setter
    def height(self, value):
        """ height
        Sets height of rectangle
        Args:
            value (int): height of rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
