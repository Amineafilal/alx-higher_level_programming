#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    number = 0
    average = 0
    for key in my_list:
        number += key[0] * key[1]
        average += key[1]
    calcul_average = number /average
    return (calcul_average)
