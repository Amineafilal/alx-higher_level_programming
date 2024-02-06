#!/usr/bin/python3
""" This module appends a string at the end  """


def append_write(filename="", text=""):
    """ This function write and append new text """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
