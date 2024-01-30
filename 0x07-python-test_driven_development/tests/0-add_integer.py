#!/usr/bin/python3
"""This module for add two integer
aaaa
a
a
a
a
a

"""

def add_integer(a, b=98):
    """ Function to add two integers.
        Argements:
        @a: The first number.
        @b: The second number. Defaults to 98.
    """
    if not (isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    if not (isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
