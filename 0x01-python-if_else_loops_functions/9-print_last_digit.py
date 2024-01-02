#!/usr/bin/python3

def print_last_digit(number):
    """Prints the last digit of a number"""
    lastnumber = abs(number) % 10
    print(lastnumber, end="")
    return(lastnumber)
