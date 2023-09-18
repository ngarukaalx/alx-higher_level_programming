#!/usr/bin/python3
# test_square.py

import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """testing instantiation"""

    def test_is_base(self):
        self.assertIsInstance(Square(7), Base)

    def test_is_rectangle(self):
        self.assertIsInstance(Square(9), Square)
