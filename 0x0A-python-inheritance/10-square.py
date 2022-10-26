#!/usr/bin/python3
"""
This module the Square class
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Class Square
    """
    def __init__(self, size):
        """
        Contructor method for Square
        Args:
            size (int): The size of the Square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Method that Returns the Square area
        """
        return (self.__size ** 2)

    def __repr__(self):
        """
        Method to get the representation
        """
        return ("[Rectangle] {:s}/{:s}"
                .format(str(self.__size),
                        str(self.__size)))
