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
        self.id = id
        Base.__nb_objects += 1
        if id is None:
            self.id = Base.__nb_objects
