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
        width (int) > 0: width of Square
        height (int) > 0: height of Square
        x (int) >= 0: x coord of Square
        y (int) >= 0: y coord of Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ __init__
        Args:
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
