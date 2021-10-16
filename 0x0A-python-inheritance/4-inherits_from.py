#!/usr/bin/python3
""" contains inherits_from function """


def inherits_from(obj, a_class):
    """ Returns true if obj's class inherits from a_class """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
