#!/usr/bin/python3
"""
This module defines add to integers


"""


def add_integer(a, b=98):
    """ Function to add two integers.
        @a: The first number :
        @b: The second number,Defaults to 98"""

    if not (isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    if not (isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
