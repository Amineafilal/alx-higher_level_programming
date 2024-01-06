#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    lenghtrev = len(my_list)
    if my_list is not None:
        for i in range(lenghtrev):
            print("{:d}".format(my_list[-i-1]))
