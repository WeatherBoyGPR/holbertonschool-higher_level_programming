#!/usr/bin/python3
""" Contains is_same_class function. """


def is_same_class(obj, a_class):
    """ Will return true is the object is exactly an instance of class """
    return type(obj) == a_class
