#!/usr/bin/python3
"""This module contains a class 'BaseGeometry'"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry



class Rectangle(BaseGeometry):
    """child class"""
    def __init__(self, width, height):
        """instantiation with and height

        args: width(positive intergers)
              height(positive intergers)
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
