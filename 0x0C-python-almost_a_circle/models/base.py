#!/usr/bin/python3
""" Contains Base class """

import json


class Base():
    """ Base
    Will serve as a base for rectangle and square classes
    Cls Attributes:
        nb_objects (int) - total number of objects
    Obj Attributes:
        id: simple id of the object
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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to_json_string
        returns json string from list_dictionaries, empty list string on None
        Args:
            list_dictionaries: a list of dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
