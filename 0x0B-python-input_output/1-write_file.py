#!/usr/bin/python3
"""This module represent  writes a string to a text file """


def write_file(filename="", text=""):
    """ This function write a lenght of characters """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
