#!/usr/bin/python3
import sys


class Square():
    def __init__(self, size=0):
        self.__size = size

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
                print("#" * self.size, file=sys.stdout)
        else:
            print()
