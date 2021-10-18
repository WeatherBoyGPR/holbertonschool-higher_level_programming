#!/usr/bin/python3
""" contains read_file function """


def read_file(filename=""):
    """ Will read a UTF8 text file and print to stdout """
    with open(filename) as f:
        for line in f:
            print(line, end='')
