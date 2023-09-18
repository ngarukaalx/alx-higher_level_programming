#!/usr/bin/python3
# test_rectangle.py
"""class module defines unittests for rectangle.py"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """testing instantiation of Rectangle class"""

    def test_rectangle_istant(self):
        self.assertIsInstance(Rectangle(2, 4), Base)

    def test_nun_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_args2(self):
        rec1 = Rectangle(7, 8)
        rec2 = Rectangle(8, 7)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_args4(self):
        rec1 = Rectangle(7, 8, 2, 3)
        rec2 = Rectangle(8, 7, 3, 2)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_args5(self):
        self.assertEqual(6, Rectangle(2, 3, 2, 4, 6).id)

    def test_setter_height(self):
        rec = Rectangle(2, 3, 2, 4, 6)
        rec.height = 7
        self.assertEqual(7, rec.height)

    def test_getter_height(self):
        rec = Rectangle(2, 3, 2, 4, 6)
        self.assertEqual(3, rec.height)

    def test_setter_with(self):
        rec = Rectangle(2, 3, 2, 4, 6)
        rec.width = 7
        self.assertEqual(7, rec.width)

    def test_getter_with(self):
        rec = Rectangle(2, 3, 2, 4, 6)
        self.assertEqual(2, rec.width)

    def test_x_getter(self):
        rec = Rectangle(2, 3, 2, 4, 6)
        self.assertEqual(2, rec.x)

    def test_x_setter(self):
        rec = Rectangle(2, 3, 2, 4, 6)
        rec.x = 0
        self.assertEqual(0, rec.x)

    def test_y_getter(self):
        rec = Rectangle(2, 3, 2, 4, 6)
        self.assertEqual(4, rec.y)

    def test_y_setter(self):
        rec = Rectangle(2, 3, 2, 4, 6)
        rec.y = 3
        self.assertEqual(3, rec.y)


class Rectangle_width(unittest.TestCase):
    """Testing width attribute"""

    def test_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(7.7, 3)

    def test_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("hiram", 3)                                                                                                                                                                            
    def test_turple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 3, 4), 4)

    def test_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"key": 3, "kiss": 4}, 3)

    def test_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([3, 3, 5, 6], 3)

    def test_None(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("None", 3)

    def test_0(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 3)

    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-2, 3)


class Rectangle_height(unittest.TestCase):
    """Testing height attribute"""

    def test_float(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(7.7, 3)

    def test_str(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle("hiram", 4)

    def test_turple(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle((1, 3, 4), 4)
    def test_dict(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle({"key": 3, "kiss": 4}, 4)

    def test_list(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle([3, 3, 5, 6], 3)

    def test_None(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle("None", 3)

    def test_0(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(0, 3)

    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(-2, 3)


class Rectangle_x(unittest.TestCase):
    """Testing x attribute"""

    def test_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 7, 2.2, 3)

    def test_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 3, "hiram", 3)

    def test_turple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 2, (1, 2, 3), 2)

    def test_dict(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 3, {"key": 3, "kiss": 4}, 2)

    def test_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 4, [3, 3, 5, 6], 6)

    def test_None(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, "None", 4)

    def test_0(self):
        with self.assertRaisesRegex(ValueError, "x must be > 0"):
            Rectangle(3, 4, 0, 3)

    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, 4, -2, 4)


class Rectangle_y(unittest.TestCase):
    """Testing y attribute"""

    def test_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 7, 2, 3.4)

    def test_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 3, 4, "hiram")

    def test_turple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 2, 4, (1, 2, 3))

    def test_dict(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 3, 5, {"key": 3, "kiss": 4})

    def test_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 4, 8, [3, 3, 5, 6])
