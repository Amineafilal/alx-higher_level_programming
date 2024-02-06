#!/usr/bin/python3
"""This module  creates an Object from a “JSON file” """

def load_from_json_file(filename):
    """ this function load json file """
    with open(filename, 'r', encoding='utf-8') as f:
        json.load(f)
