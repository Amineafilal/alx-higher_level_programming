#!/usr/bin/python3
"""This module contains inherits from BaseGeometry"""

class BaseGeometry:
    """Class of base geometry"""
    def area(self):
        """
        Compute the area of the geometry.

        Raises:
        Exception: Indicates that the area() method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate an integer value.

        Args:
        name (str): The name of the value being validated.
        value: The value to be validated.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


        class Rectangle(BaseGeometry):
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
                self.integer_validator("height", height)
                self.__width = width
                self.__height = height
