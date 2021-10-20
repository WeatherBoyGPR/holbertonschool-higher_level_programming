#!/usr/bin/python3
""" Contains Square class """

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square
    Represents a square
    Cls Attributes:
        nb_objects (int) - total number of objects
    Obj Attributes:
        id: simple id of the object
        size (int) > 0: size of Square
        width (int) > 0: width of Square
        height (int) > 0: height of Square
        x (int) >= 0: x coord of Square
        y (int) >= 0: y coord of Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ __init__
        Args:
            size (int) > 0: size of Square
            width (int) > 0: width of Square
            height (int) > 0: height of Square
            x (int): x position of Square
            y (int): y position of Square
            id (int): specified id of Square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns string representation of Square instance """
        return (
            "[Square] (" + str(self.id) + ") " + str(self.x) + "/" +
            str(self.y) + " - " + str(self.height)
        )

    def to_dictionary(self):
        """ Returns dictionary representation of square """
        return (
            {
                'id': self.id, 'size': self.size,
                'x': self.x, 'y': self.y
            }
        )

    def update(self, *args, **kwargs):
        """ update
        Can update any value in below order:
        id, size (int), x (int), y (int)
        """
        if args and len(args) > 0:
            i = 0
            for rot in args:
                i += 1
                if i == 1:
                    setattr(self, "id", rot)
                    continue
                elif i == 2:
                    self.size = rot
                    continue
                elif i == 3:
                    self.x = rot
                    continue
                elif i == 4:
                    self.y = rot
                    break

        elif kwargs and len(kwargs) > 0:
            for key, val in kwargs.items():
                if key is "id":
                    setattr(self, "id", val)
                    continue
                elif key is "size":
                    self.size = val
                    continue
                elif key is "x":
                    self.x = val
                    continue
                elif key is "y":
                    self.y = val
                    continue

    @property
    def size(self):
        """ Getter for size """
        return self.height

    @size.setter
    def size(self, value):
        """ Setter for size """
        self.integer_validation(value, "width")
        self.height = value
        self.width = value
