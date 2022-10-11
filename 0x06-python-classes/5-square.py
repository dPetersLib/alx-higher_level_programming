#!/usr/bin/python3
"""OOP implementation of Square

This module models a square. The square has been initialized with a size.
Note that this documentation must come before anything else.
"""
import sys


class Square:
    """A class that defines a square

    The Square is initialised with a size with its default being 0.
    It has an <area> method which calculates and returns
    the area of the square.
    It also has a getter and setter methods to access and update
    the size of the Square.
    Lastly it has a <my_print> method to print out a
    pattern according to the size.

    """
    def __init__(self, size=0):
        """This is our class constructor method.

        This constructor method is call just once,
        i.e. when an instance of this class is initiated.

        Args:
            size (int): This is the size of the Square instance.

        """
        self.__size = size

    def area(self):
        """This method calculates the Area of the Square

        Return:
            The square of the size; i.e size * size/
        """
        return self.__size * self.__size

    @property
    def size(self):
        """int: this is the size of the Square."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints a pattern according to the size

        This method prints in stdout the square with the character (#)

        """
        if self.size > 0:
            for i in range(self.size):
                print("#" * self.size, file=sys.stdout)
        else:
            print()
