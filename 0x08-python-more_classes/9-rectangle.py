#!/usr/bin/python3
""" Module that contains Rectangle Class. """


class Rectangle:
    """ Acts as a Rectangle.

    Attributes:
        number_of_instances (int): Total number of Rectangle objects
        print_symbol (str): symbol to represent rectangle with
    """

    number_of_instances = 0
    print_symbol = "#"

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
        type(self).number_of_instances += 1

    def __del__(self):
        """ Performs deletion processes. """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    def __str__(self):
        """ Returns a printable string representation of the Rectangle. """
        if self.__width * self.__height == 0:
            return("")
        res = []

        for h in range(self.__height):
            res.append((str(self.print_symbol) * self.__width))
        return ("\n".join(res))

    def __repr__(self):
        """ Returns a literal string representation of the Rectangle. """
        bet = str(self.__width) + ", " + str(self.__height)
        return("Rectangle(" + bet + ")")

    @classmethod
    def square(cls, size=0):
        """ Returns a square rectangle. """
        return cls(size, size)

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

    def area(self):
        """ Will calculate the area of the Rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ Will calculate the perimeter of the Rectangle """
        if self.__height * self.__width == 0:
            return 0
        return ((self.__height + self.__width) * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ bigger_or_equal
        Compares the area of two rectangles, returns rect 1 if equal
        Args:
            rect_1 (Rectangle): first rectangle to compare
            rect_2 (Rectangle): second rectangle to compare
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
