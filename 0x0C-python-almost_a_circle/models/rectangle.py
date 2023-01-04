#!/usr/bin/python3
"""Rectangle class."""

from .base import Base


class Rectangle(Base):
    """Rectangle class."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """This is our class constructor method.

        When called, it calls the constructor of the Base class.

        Args:
            width (int): This is the width of the rectangle instance.
            height (int): This is the height of the rectangle instance.
            x (int): This is the x point of the rectangle instance.
            y (int): This is the y point of the rectangle instance.

        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """int: this is the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """int: this is the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """int: this is the x point of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """int: this is the y point of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """This method calculates the Area of the rectangle

        Return:
            The area of the rectangle; i.e width * height/
        """
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with the
        character #
        """
        for i in range(self.__height):
            print("#" * self.__width)
