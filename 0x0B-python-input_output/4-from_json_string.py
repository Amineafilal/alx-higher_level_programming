#!/usr/bin/python3
""" This module represent returns an object (Python data structure) """
import json


def from_json_string(my_str):
    """ This function json string """
    return json.loads(my_str)
