#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_delete = [key for key, val in a_dictionary.items() if val == value]

    for key in key_delete:
        if value == a_dictionary.get(key):
            del a_dictionary[key]
