#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    lenghtrev = len(my_list)
    for i in range(1, lenghtrev + 1):
        print("{}".format(my_list[-i]))
