#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class that defines testmaxinterger"""

    def test_with_positive(self):
        """Test when the list is of positive numbers"""
        result = max_integer([2, 3, 4, 5, 6])
        self.assertEqual(result, 6)

    def test_empty(self):
        """Test when list is empty"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_none_entry(self):
        """Test with None input"""

    def test_negative_int(self):
        """Test with negative int"""
        result = [4, 3, 2, 1]
        self.assertEqual(max_integer(result), 4)

    def test_string(self):
        """Test with string"""
        result = "hiram"
        self.assertEqual(max_integer(result), 'r')


if __name__ == '__main__':
    """To be executed if this module treated as main"""

    unittest.main()
