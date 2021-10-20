#!/usr/bin/python3
""" Holds unit tests for base class """

import unittest
from models.base import Base


class TestBaseClassinit(unittest.TestCase):
    """ Class for testing the Base Class """

    def test_basic_creation(self):
        """ tests most basic creation case """
        testc = Base()
        self.assertTrue(type(testc) is Base)
        self.assertEqual(testc.id, 1)

    def test_multicreation(self):
        """ tests creation of several base classes """
        testc1 = Base()
        testc2 = Base()
        testc3 = Base()
        self.assertEqual(testc1.id, testc2.id - 1, testc3.id -2)

    def test_specified_id(self):
        """ Tests specified id """
        testc1 = Base(32)
        testc2 = Base(2)
        testc3 = Base()
        self.assertEqual(testc1.id, 32)
        self.assertEqual(testc2.id, 2)
        self.assertEqual(testc3.id, 7)

if __name__ == "__main__":
    unittest.main()
