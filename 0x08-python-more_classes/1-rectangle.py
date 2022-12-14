#!/usr/bin/python3
"""1-rectangle module.

Based on the first 0-rectangle.

"""


class Rectangle:
    """Real Rectangle.

    Defines a real rectangle.
    """

    def __init__(self, width=0, height=0):
        """Instantiate a rectangle.

        This constructor method is call just once,
        i.e. when an instance of this class is initiated.

        Args:
            width (int): width of the rectangle instance.
            height (int): height of the rectangle.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Width property of a Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height property of a Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
