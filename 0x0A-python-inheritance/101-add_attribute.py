#!/usr/bin/python3
""" This module adds a new attribute to an object """


def add_attribute(obj, attribute, value):
    """ Check if the object can have a new attribute"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
