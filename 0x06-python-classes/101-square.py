#!/usr/bin/python3
"""A Square based on the module : 6-square

This module models a square. The square has been initialized with a size, \
and a position attributes.
The new thing about this module is that \
the Square instance representation will have \
the same behavior as its my_print() method.
"""


class Square:
    """A class that defines a square

    The Square is initialised with a size and position with their default
    being 0 and (0, 0) respectively.
    It has an <area> method which calculates and returns
    the area of the square.
    It has a getter and setter methods to access and update
    the size of the Square.
    It has a <my_print> method to print out a
    pattern according to the size.
    It has a getter and setter methods to access and update
    the position of the Square.

    """
    def __init__(self, size=0, position=(0, 0)):
        """This is our class constructor method.

        This constructor method is call just once,
        i.e. when an instance of this class is initiated.

        Args:
            size (int): This is the size of the Square instance.
            position (tuple): This is the position of the Square instance.

        """
        self.__size = size
        self.__position = position

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
        
        Note:
            If size is equal to 0, print an empty line
            position should be use by using space
            Don’t fill lines by spaces when position[1] > 0

            The last condition above is yet to be implemented
            as it isn't clearly understood. This is because the
            same case provided goes against the condition, and when
            implemented, it failed to pased some tests.

        """
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                # if self.position[0] > 0 and self.position[1] == 0:
                print(" " * self.position[0], end="")
                print("#" * self.size)

    @property
    def position(self):
        """tuple: this is the position of the Square."""
        return self.__position

    @position.setter
    def position(self, value):
        is_ok = False
        if type(value) == tuple and len(value) == 2:
            is_ok = True
            for i in value:
                if type(i) != int or i <= 0:
                    is_ok = False
                    break
        if is_ok:
            self.__property = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
    
    def __str__(self):
        self.my_print()
        return ""