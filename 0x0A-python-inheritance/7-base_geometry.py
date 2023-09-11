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
        
