#!/usr/bin/python3

""" This module defines the object is an instance"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or if the object is an instance.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a_class or any subclass.
    """
    return isinstance(obj, a_class)
