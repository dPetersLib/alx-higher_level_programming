#!/usr/bin/python3
"""8-rectangle module.

Based on the previous `7-rectangle`.

"""


class Rectangle:
    """Real Rectangle.

    Defines a real rectangle.
    """

    number_of_instances = 0
    """This keeps track of all instances of Rectangle class"""

    print_symbol = "#"
    """Denotes the symbol to be printed to represent the Rectangle parameter"""

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
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """Informal representation of the rectangle

        This prints # according to the perimeter of the rectangle.
        """
        if self.perimeter() > 0:
            for i in range(self.height - 1):
                print(self.print_symbol * self.width)
            print(self.print_symbol * self.width, end="")
        return ""

    def __repr__(self):
        """Formal representation of the rectangle

        This returns a string representation of the rectangle
        to be able to recreate a new instance by using eval()
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Deconstructor

        This is the deconstructor for a Rectangle object.
        It is called just before the instance is being deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Rectangle Equality check

        Checks for the greater rectangle.

        Args:
            rect_1 (Rectangle) : the first rectangle instance.
            rect_2 (Rectangle) : the second rectangle instance.

        Return:
            It returns the greater rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1
