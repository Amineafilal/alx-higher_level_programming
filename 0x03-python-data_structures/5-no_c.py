#!/usr/bin/python3
def no_c(my_string):

    no_cs = ""
    for i in range(len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            no_cs += my_string[i]
    return (no_cs)
