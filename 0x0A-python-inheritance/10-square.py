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
