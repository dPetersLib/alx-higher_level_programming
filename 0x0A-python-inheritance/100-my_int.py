#!/usr/bin/python3
"""
Module for the MyInt class
"""


class MyInt(int):
    """
    Class MyInt
    """

    def __init__(self, value):
        """
        Constructor method
        Args:
            value (int): The value of this class
        """
        if isinstance(value, int):
            self.__int = value

    def __ne__(self, value):
        """
        Method for the != conditional
        Returns:
            True
        """
        return True

    def __eq__(self, value):
        """
        Method for the == conditional
        Returns:
            False
        """
        return False
