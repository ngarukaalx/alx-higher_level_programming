#!/usr/bin/python3
"""This module contains a class 'BaseGeometry'"""


class BaseGeometry:
    """defines a class"""

    def area(self):
        """Raise an exception message"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value

        args: name - assuming its always a string
              value(interger) - value

        raise: TypeError if value is not an integer
               ValueError if value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """child class"""
    def __init__(self, width, height):
        """instantiation with and height

        args: width(positive intergers)
              height(positive intergers)
        """
        super().__init__(width, height)
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
