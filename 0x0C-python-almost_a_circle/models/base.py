#!/usr/bin/python3
""" Contains Base class """


class Base():
    """ Base
    Will serve as a base for rectangle and square classes
    Cls Attributes:
        nb_objects (int) - total number of objects
    Obj Attributes:
        id (int): simple id of the object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ __init__
        Args:
            id (int)/(None): object id, defaults to nb_objects+1 on None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
