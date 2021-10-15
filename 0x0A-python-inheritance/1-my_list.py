#!/usr/bin/bash
""" Contains MyList Class """


class MyList(list):
    """ Adds sorted printing to list class """

    def print_sorted(self):
        """ Will print a sorted list """
        print(sorted(self))
