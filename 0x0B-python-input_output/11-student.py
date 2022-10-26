#!/usr/bin/python3
"""
Module for the class Student
"""


class Student:
    """
    Class Student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Function that returns the dictionary description
        Returns:
            The dictionary description
        """
        a_dict = {}
        if attrs is None:
            return self.__dict__
        for i in attrs:
            if hasattr(self, i):
                a_dict[i] = getattr(self, i)
        return a_dict

    def reload_from_json(self, json):
        """
        Public method that replaces all attributes of the Student instance.
        Args:
            json: Info in JSON format
        """
        for key, val in json.items():
            if hasattr(self, key):
                setattr(self, key, val)
