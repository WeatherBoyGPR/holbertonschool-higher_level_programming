#!/usr/bin/python3
""" Contains lookup function """


def lookup(obj):
    """ Will return a list of available attributes and methods of obj """
    return list(dir(obj))
