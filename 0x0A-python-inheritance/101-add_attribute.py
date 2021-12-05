#!/usr/bin/python3
""" holds add_attribute function """


def add_attribute(ob, attr, val):
    """ Will add attribute attr to object ob if possible """
    if hasattr(ob, "__dict__"):
        setattr(ob, attr, val)
    else:
        raise TypeError("can't add new attribute")
