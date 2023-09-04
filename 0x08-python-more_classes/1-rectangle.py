#!/usr/bin/python3
"""Defines a rectacle"""


class Rectangle:
    """class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Instantiation width optional width and height

        args: width (int): the rectangles width
              height (int): the height of rectangle
        """

        if isinstance(width, int) and width >= 0:
            self.width = width
        else:
            if not isinstance(width, int):
                raise TypeError("width must be an integer")
            if width < 0:
                raise ValueError("width must be >= 0")
        if isinstance(height, int) and height >= 0:
            self.height = height
        else:
            if not isinstance(height, int):
                raise TypeError("height must be an integer")
            if height < 0:
                raise ValueError("height must be >= 0")

    @property
    def height(self):
        """fuction to retrive height"""

        return self.__height

    @height.setter
    def height(self, value):
        """fuction to set height"""

        if value < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__height = value

    @property
    def width(self):
        """fuction to retrive height"""

        return self.__width

    @width.setter
    def width(self, value):
        """fuction to set witdth"""

        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.__width = value
