#!/usr/bin/python3
def uppercase(str):
    """Write a function that prints a string in uppercase"""
    stock = ""
    for u in str:
        if ord(u) >= 97 and ord(u) <= 123:
            u = chr(ord(u) - 32)
            stock += chr(ord(u))
        else:
            stock += chr(ord(u))
    print("{}".format(stock))
