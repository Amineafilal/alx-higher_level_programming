#!/usr/bin/python3
"""This modulle represent inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file after each line a specific string."""
    with open(filename, 'r') as f:
        lines = f.readlines()

    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
