#!/usr/bin/python3
"""This module  creates an Object from a “JSON file” """
import json
def load_from_json_file(filename):
    """ this function load json file """
    with open(filename) as f:
     return json.load(f)
