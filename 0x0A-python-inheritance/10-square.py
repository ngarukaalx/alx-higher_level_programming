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
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculates the area"""
        return self.__width * self.__height

    def __str__(self):
        """returns string representation"""
        return (f"[Rectangle] {self.__width}/{self.__height}")


class Square(Rectangle):
    """grandchild"""
    def __init__(self, size):
        """constructor
        args: size(positive interger)
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """calculates area of square"""
        return self.__size * self.__size
