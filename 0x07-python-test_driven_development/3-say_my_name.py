#!?usr/bin/python
""" This module holds the say_my_name function. """


def say_my_name(first_name, last_name=""):
    """ say_my_name
    Args:
        first_name (string): first name to print
        last_name (string: second name to print
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
