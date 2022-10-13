#!/usr/bin/python3
"""A Square based on the module: 4-square

The instances of this Square can answer to comparators:
==, !=, >, >=, < and <= based on the square area.
"""


class Square:
    """A class that defines a square

    The Square is initialised with a size with its default being 0.
    It also has an <area> method which calculates and returns
    the area of the square.
    It also has a getter and setter methods to access and update
    the size of the Square

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
        if type(value) not in [int, float]:
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """Equivalence check

        It check for equivalence between two instances of the Sqaure.

        Args:
            other (Square): the second instance.

        Return:
            True if self.area and other.area are equivalent.
            False if otherwise.
        """
        if self.area() == other.area():
            return True
        return False

    def __gt__(self, other):
        """Greater Than check

        It mimics the '>' sign between two instances of the Square.

        Args:
            other (Square): the second instance.

        Return:
            True if self.area is greater than other.area
            False if otherwise.
        """
        if self.area() > other.area():
            return True
        return False

    def __ge__(self, other):
        """Greater Than or Equal to check

        It mimics the '>=' sign between two instances of the Square.

        Args:
            other (Square): the second instance.

        Return:
            True if self.area is greater than or equal to other.area
            False if otherwise.
        """
        if self.area() >= other.area():
            return True
        return False

    def __lt__(self, other):
        """Less Than check

        It mimics the '<' sign between two instances of the Square.

        Args:
            other (Square): the second instance.

        Return:
            True if self.area is less than  other.area
            False if otherwise.
        """
        if self.area() < other.area():
            return True
        return False

    def __le__(self, other):
        """Less Than check

        It mimics the '<=' sign between two instances of the Square.

        Args:
            other (Square): the second instance.

        Return:
            True if self.area is less than or equal to other.area
            False if otherwise.
        """
        if self.area() <= other.area():
            return True
        return False

    def __ne__(self, other):
        """Less Than check

        It mimics the '!=' sign between two instances of the Square.

        Args:
            other (Square): the second instance.

        Return:
            True if self.area is not equal to other.area
            False if otherwise.
        """
        if self.area() != other.area():
            return True
        return False
