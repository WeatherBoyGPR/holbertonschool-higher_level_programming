#!/usr/bin/python3
""" Contains append_write function """


def append_write(filename="", text=""):
    """ append_write
    Will append a string to the end of a file in UTF8 encoding
    Args:
        filename (str): target file
        text (str): text to append
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
