#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        """
Initializes a new Square instance.

Parameters:
- size (int, optional): The size of the square. Default is 0.

Raises:
- TypeError: If the provided size is not an integer.
- ValueError: If the provided size is less than 0.
"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
