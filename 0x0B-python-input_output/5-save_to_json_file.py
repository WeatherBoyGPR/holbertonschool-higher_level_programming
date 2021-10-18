#!/usr/bin/python3
""" contains save_to_json_file function """
import json


def save_to_json_file(my_obj, filename):
    """ save_to_json_file
    Will write a json representative of an object to a file.
    Args:
        my_obj (any object): object to write to file
        filename (str): file to write object to
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
