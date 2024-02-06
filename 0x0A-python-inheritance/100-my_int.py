#!/usr/bin/python3
"""This module definesvthat inherits from int"""


class MyInt(int):
    """ class of int """

    def __eq__(self, other):
        """Override operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """ Overide operator"""
        return super().__eq__(other)
