#!/usr/bin/python3
""" Contains Rectangle class """

from models.base import Base


class Rectangle(Base):
    """ Rectangle
    Represents a rectangle
    Cls Attributes:
        nb_objects (int) - total number of objects
    Obj Attributes:
        id: simple id of the object
        width (int) > 0: width of rectangle
        height (int) > 0: height of rectangle
        x (int) >= 0: x coord of rectangle
        y (int) >= 0: y coord of rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ __init__
        Args:
            width (int) > 0: width of rectangle
            height (int) > 0: height of rectangle
            x (int): x position of rectangle
            y (int): y position of rectangle
            id (int): specified id of rectangle
        """
        self.integer_validation(width, "width")
        self.integer_validation(height, "height")
        self.integer_validation(x, "x", True)
        self.integer_validation(y, "y", True)
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def __str__(self):
        """ Returns string representation of Rectangle instance """
        return (
            "[Rectangle] (" + str(self.id) + ") " + str(self.x) + "/" +
            str(self.y) + " - " + str(self.width) + "/" + str(self.height)
        )

    def update(self, *args):
        """ update
        Can update any value in below order:
        id, width (int), height (int), x (int), y (int)
        """
        i = 0
        for rot in args:
            i += 1
            if i == 1:
                setattr(self, "id", rot)
            if i == 2:
                self.integer_validation(rot, "width")
                self.__width = rot
            if i == 3:
                self.integer_validation(rot, "height")
                self.__height = rot
            if i == 4:
                self.integer_validation(rot, "x", True)
                self.__x = rot
            if i == 5:
                self.integer_validation(rot, "y", True)
                self.__y = rot

    def integer_validation(self, value, name="FORGOT", posi=False):
        """ integer_validation
        Will test if value is valid, has two modes to modulate if 0 is valid
        Raises TypeError or ValueError if non-valid
        Args:
            name (str): name of value
            value (int): value to test
            posi (bool): whether or not the value represents a position
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if posi is True:
            if value < 0:
                raise ValueError(name + " must be >= 0")
        else:
            if value <= 0:
                raise ValueError(name + " must be > 0")

    def area(self):
        """ Returns area of Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """ Displays a representation of Rectangle instance """
        print(
            ("\n" * self.__y) +
            ((' ' * self.__x) + ("#" * self.__width) + "\n") * self.__height,
            end=''
        )

    @property
    def width(self):
        """ Getter method for width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter method for width attribute """
        self.integer_validation(value, "width")
        self.__width = value

    @property
    def height(self):
        """ Getter method for height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter method for height attribute """
        self.integer_validation(value, "height")
        self.__height = value

    @property
    def x(self):
        """ Getter method for x attribute """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter method for x attribute """
        self.integer_validation(value, "x", True)
        self.__x = value

    @property
    def y(self):
        """ Getter method for y attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter method for y attribute """
        self.integer_validation(value, "y", True)
        self.__y = value
