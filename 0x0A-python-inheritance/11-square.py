#!/usr/bin/python3
"""This module contains a class 'BaseGeometry'"""
Rectangle = __import__('9-rectangle').Rectangle


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

    def __str__(self):
        """returns string representation of square"""
        return (f"[Square] {self.__size}/{self.__size}")
