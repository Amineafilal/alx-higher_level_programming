#!/usr/bin/python3
"""This module contains  integer validator"""


class BaseGeometry:
    """ class of base geometry"""
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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
