#!/usr/bin/python3
""" contains BaseGeometry class v2 """


class BaseGeometry():
    """ Base collector  """

    def area(self):
        """ does nothing but complain """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value as integer """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
