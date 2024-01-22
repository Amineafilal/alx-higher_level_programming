#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        resu = fct(*args)
    except Exception as msger:
        print("Exception: {}".format(msger))
        resu = None
    return (resu)
