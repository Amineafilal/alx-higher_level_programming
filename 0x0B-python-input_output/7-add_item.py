#!/usr/bin/python3
""" Addds all arguments to a Python list """
import sys
import json
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"
my_list = []
if path.exists(filename):
    my_list = load_from_json_file
my_list.extend(sys.argv[1:])
save_to_json_file(my_list, filename)
