#!/usr/bin/python3
"""Magic Class Module - This module contains our magic class."""
import math


class MagicClass:
    """This is the class models a ByteCode given provided for the task."""
    def __init__(self, radius):
        """This is the constructor of the class and it is called once."""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self._MagicClass__radius = radius

    def area(self):
        """This calculates and returns the area. The result is a float."""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """This calculates and returns the circumference of type float."""
        return 2 * math.pi * self._MagicClass__radius
