#!/usr/bin/python3
"""This module contains inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class inherits from BaseGeometry"""
    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.

        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

        Raises:
        TypeError: If width or height are not integers.
        ValueError: If width or height are less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Compute the area of the rectangle.

        Returns:
            int: The area of the rectangle.
            """
        return self.__width * self.__height

    def __str__(self):
        """
        Return the string representation of the rectangle.

        Returns:
        str: The string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
