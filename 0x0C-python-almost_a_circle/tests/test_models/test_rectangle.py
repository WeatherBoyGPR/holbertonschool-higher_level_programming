#!/usr/bin/python3
""" Holds unit tests for rectangle class """

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleClassinit(unittest.TestCase):
    """ Class for testing Rectangle object creation """

    def test_basic_creation(self):
        """ Tests most basic creation case """
        testc = Rectangle(10, 20)
        self.assertTrue(type(testc) is Rectangle)
        self.assertEqual(testc.id, 6)

if __name__ == "__main__":
    unittest.main()
