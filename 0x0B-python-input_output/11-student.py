#!/usr/bin/python3
"""This module contains a class Student that defines a student"""


class Student:
    """class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age

        args: first_name
              last_name
              age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""

        if attrs is not None and isinstance(attrs, list)\
                and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

        else:
            return vars(self)

    def reload_from_json(self, json):
        """def reload_from_json(self, json)

        args: json(dict) - dictionary
        """
        if isinstance(json, dict):
            for key, value in json.items():
                setattr(self, key, value)
