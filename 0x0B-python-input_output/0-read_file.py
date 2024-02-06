#!/usr/bin/python3
"""This module represents a read file"""


def read_file(filename=""):
    """This function read a file"""
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
