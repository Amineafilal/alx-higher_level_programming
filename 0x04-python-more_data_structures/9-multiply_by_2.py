#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multip_two = {key: a_dictionary[key] * 2 for key in a_dictionary}
    return multip_two
