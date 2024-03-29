#!/usr/bin/python3

""" This module contains a class Square that defines a square"""


class Square:
    """Represents a square withe a size and provides methods"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2
