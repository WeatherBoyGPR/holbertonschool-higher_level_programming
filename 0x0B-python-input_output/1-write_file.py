#!/usr/bin/python3
""" contains write_file function """


def write_file(filename="", text=""):
    """ Will write text into a file """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
