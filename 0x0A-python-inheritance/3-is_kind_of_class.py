#!/usr/bin/python3
""" contains is_kind_of_class function """


def is_kind_of_class(obj, a_class):
    """returns true is obj is instance of a_class or inherited from a_class"""
    return isinstance(obj, a_class)
