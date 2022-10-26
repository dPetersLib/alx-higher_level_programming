#!/usr/bin/python3
"""
Module for BaseGeometry class.
"""


class BaseGeometry:
    """
    Class BaseGeometry
    """
    def area(self):
        """
        Method: def area(self): that raises an Exception with the message
        area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method def integer_validator(self, name, value) that validates value
        Args:
            name (str): The name
            value (int): The value
        """
        if not isinstance(name, str):
            raise TypeError("The first parameter must be an string")
        if not isinstance(value, int) or value.__class__ is bool:
            raise TypeError("{:s} must be an integer" .format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
