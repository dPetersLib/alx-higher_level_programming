#!/usr/bin/python3
import sys


class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.size > 0:
            for i in range(self.size):
                if self.position[0] > 0:
                    print(" " * self.position[0], end="", file=sys.stdout)
                print("#" * self.size, file=sys.stdout)
        else:
            print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        is_ok = False
        if type(value) == tuple and len(value) == 2:
            is_ok = True
            for i in value:
                if type(i) != int or type(i) <= 0:
                    is_ok = False
                    break
        if is_ok:
            self.__property = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
