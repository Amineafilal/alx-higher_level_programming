#!/usr/bin/python3
from sys import stderr
def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as msger:
        print("Exception: {}".format(msger))
        return None
