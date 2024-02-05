#!/usr/bin/python3
"""This module represents  that raises an Exception with the message"""


class BaseGeometry:
    """ This class of base geometry"""
    def area(self):
        """
        Compute the area of the geometry.

        Raises:
        Exception: Indicates that the area() method is not implemented.
        """
        raise Exception("area() is not implemented")
