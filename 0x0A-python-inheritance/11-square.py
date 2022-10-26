#!/usr/bin/python3
"""
This module for the Square class
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Class Square
    """

    def __init__(self, size):
        """
        Constructor method that returns an instance of a Square class
        Args:
            size (int): The size of the Square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Method that returns the Square area
        """
        return (self.__size ** 2)

    def __repr__(self):
        """
        Method to get the representation
        """
        return ("[Square] {:s}/{:s}"
                .format(str(self.__size),
                        str(self.__size)))
