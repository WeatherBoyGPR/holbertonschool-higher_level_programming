#!/usr/bin/python3
""" Contains load_from_json_file function """
import json


def load_from_json_file(filename):
    """ Will load a single object from a json file """
    with open(filename, encoding='utf-8') as f:
        return json.loads(f)
