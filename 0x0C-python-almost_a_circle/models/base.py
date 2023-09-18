#!/usr/bin/python3
"""This module contains Class base"""
import json


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor

        args:
             id(interger) -  public instance
        """
        if id is not None:
            self.id = id
        else:
            Base. __nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []

        class_name = cls.__name__
        file_name = f"{class_name}.json"
        dict_list = [obj.to_dictionary() for obj in list_objs]
        string_json = cls.to_json_string(dict_list)

        with open(file_name, "w", encoding='utf-8') as my_file:
            my_file.write(string_json)

    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        file_name = f"{cls.__name__}.json"

        try:
            with open(file_name, 'r', encoding='utf-8') as my_file:
                json_string = my_file.read()
                json_list = cls.from_json_string(json_string)
                instance_list = [cls.create(**d) for d in json_list]
                return instance_list
        except FileNotFoundError:
            return []
