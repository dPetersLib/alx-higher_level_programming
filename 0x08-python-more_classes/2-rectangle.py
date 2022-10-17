#!/usr/bin/python3
"""2-rectangle module.

Based on the first `2-rectangle`.

"""


from turtle import width


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
        self.__height = height
        self.__width = width

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

    def area(self):
        """Area of the Rectangle.

        This calculates the area of the rectangle.

        Return:
            the area.
        """
        return self.width * self.height

    def perimeter(self):
        """Perimeter of the Rectangle.

        This calculates the perimeter of the rectangle.

        Return:
            the perimeter or zero if either width of height is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
