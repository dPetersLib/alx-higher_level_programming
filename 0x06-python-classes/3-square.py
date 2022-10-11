#!/usr/bin/python3
"""OOP implementation of Square

This module models a square. The square has been initialized with a size.
"""


class Square:
    """A class that defines a square

    The Square is initialised with a size with its default being 0.

    """

    def __init__(self, size=0):
        """This is our class constructor method.

        This constructor method is call just once,
        i.e. when an instance of this class is initiated.

        Args:
            size (int): This is the size of the Square instance.

        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # private attribute

    def area(self):
        """This method calculates the Area of the Square

        Return:
            The square of the size; i.e size * size/
        """
        return self.__size * self.__size
