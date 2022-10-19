#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 8]), 8)
        self.assertIsNone(max_integer([]))
        self.assertNotEqual(max_integer([0, 2, 1, 1]), 1)
