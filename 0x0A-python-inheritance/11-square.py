#!/usr/bin/python3
"""This module contains inherits from BaseGeometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class inherits from BaseGeometry"""

    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
        size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
