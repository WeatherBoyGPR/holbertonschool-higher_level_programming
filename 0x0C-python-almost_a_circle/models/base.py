#!/usr/bin/python3
""" Contains Base class """

import json
import os


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

    @staticmethod
    def from_json_string(json_string):
        """ returns list of dictionaries from json string representation """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes json string of a list of rectangles/squares to a file """
        if list_objs is None:
            with open(cls.__name__ + ".json", 'w', encoding='utf-8') as f:
                f.write(cls.to_json_string(list_objs))
                return
        dlist = [cls.to_dictionary(a) for a in list_objs]
        with open(cls.__name__ + ".json", 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(dlist))

    @classmethod
    def load_from_file(cls):
        """ Loads json representations of instances from file """
        s = ".json"
        if os.path.exists(str(cls.__name__) + s):
            with open(str(cls.__name__) + s, encoding='utf-8') as f:
                i = cls.from_json_string(f.read())
                return [cls.create(**ob) for ob in i]
        return []

    @classmethod
    def create(cls, **dictionary):
        """ Returns class instance with attributes preset """
        if cls.__name__ is "Square":
            res = cls(1)
        if cls.__name__ is "Rectangle":
            res = cls(1, 1)
        res.update(**dictionary)
        return res
