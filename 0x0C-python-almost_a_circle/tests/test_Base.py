#!/usr/bin/python3
"""This module for base test suite"""


import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Base class."""

    def test_no_arg(self):
        b = Base()
        b1 = Base()
        self.assertEqual(b.id, b1.id - 1)
