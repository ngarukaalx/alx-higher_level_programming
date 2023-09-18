#!/usr/bin/python3
"""This module contains a class that inherits from Rectangle"""
from .rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """class constructor
        args:
            size - size of square
            x - x cordinate
            y - y cordinate
            id - id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str representation of a square"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size

        Args:
        value (int): size value to set
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update arguments using args and kwargs"""

        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
