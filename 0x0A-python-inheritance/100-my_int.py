#!/usr/bin/python3
""" Holds MyInt class """


class MyInt(int):
    """ Acts as int class, with inverted logical = operators """

    def __eq__(self, object2):
        """ inverted == """
        return self.real != object2

    def __ne__(self, object2):
        """ inverted != """
        return self.real == object2
