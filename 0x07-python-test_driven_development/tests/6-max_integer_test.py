#!/bin/usr/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class max_integer_test(unittest.TestCase):
    """ 6-max_integer_test """

    def test_basic(self):
        """ basic input test """
        self.assertEqual(max_integer([1, 80, 9, 23, 0]), 80)

    def test_empty_list(self):
        """ empty list test """
        self.assertEqual(max_integer([]), None)

    def test_negative_numbers(self):
        """ list with negative numbers test """
        self.assertEqual(max_integer([-4, -7, -9, -1]), -1)

    def test_mixed_numbers(self):
        """ list with both negative and positive numbers test """
        self.assertEqual(max_integer([5, -6, 3, 0, 15]), 15)

if __name__ == '__main__':
    unittest.main()
