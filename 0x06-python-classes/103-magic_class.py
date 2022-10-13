#!/usr/bin/python3
"""Magic Class Module - This module contains our magic class"""
import math


class MagicClass:
    """MagicClass class"""
    def __init__(self, radius):
        """This is the constructor of the class"""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self._MagicClass__radius = radius

    def area(self):
        """this calculates and returns the area"""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """this calculates and returns the circumference"""
        return 2 * math.pi * self._MagicClass__radius
