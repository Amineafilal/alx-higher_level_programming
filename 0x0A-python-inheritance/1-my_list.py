#!/usr/bin/python3
"""This module defines a custom list class and a function."""


class MyList(list):
    """ Print sorted in the class"""
    def print_sorted(self):
        print(sorted(self))
