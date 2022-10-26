#!/usr/bin/python3
"""
Module for class Rectangle
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rectangle
    """

    def __init__(self, width, height):
        """
        Contrunctor method for Class Rectangle
        Args:
            width (int): The width of the Rectangle
            height (int): The height of the Rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Method that returns the Rectangle area
        """
        return (self.__width * self.__height)

    def __repr__(self):
        """
        Method to get the representation of the Rectangle
        """
        return ("[Rectangle] {:s}/{:s}"
                .format(str(self.__width),
                        str(self.__height)))
