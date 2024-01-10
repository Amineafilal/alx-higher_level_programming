#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    number_value = sorted(a_dictionary.keys())
    for key in number_value:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
