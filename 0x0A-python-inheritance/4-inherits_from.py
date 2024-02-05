#!/usr/bin/python3
""" This module represents  function that returns True"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a class that inherited.
    """
    return (
        isinstance(obj, type) and issubclass(type(obj), a_class) and
        type(obj) is not a_class
    )
