#!/usr/bin/python3
"""
1-rectangle module
==================

Based on the first `0-rectangle`

"""


class Rectangle:
    """Real Rectangle
    Defines a real rectangle
    """
    def __init__(self, width=0, height=0):
        """Instantiation method
        Args:
            width (int): width of the rectangle instance
            height (int): height of the rectangle
        """
        self.__width = width
        self.__height = height

    def width(self):
        """Width property of a Rectangle
        Return:
            private instant attribute `width`
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    def height(self):
        """Height property of a Rectangle
        Return:
            private instant attribute `height`
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value
