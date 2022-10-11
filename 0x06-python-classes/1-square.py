#!/usr/bin/python3
"""OOP implementation of Square

This module models a square. The square has been initialized with a size.
"""


class Square:
    """A class that defines a square

    The Square is initialised with a size (no type/value verification).
    
    """

    def __init__(self, size):
        """This is our class constructor method.

        This constructor method is call just once,
        i.e. when an instance of this class is initiated.

        Args:
            size (int): This is the size of the Square instance.
        
        """
        self.__size = size  # private attribute
