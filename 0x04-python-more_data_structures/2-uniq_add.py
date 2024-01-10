#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_sum = 0
    for x in set(my_list):
        unique_sum += x
    return (unique_sum)
