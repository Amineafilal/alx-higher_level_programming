#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        resu = fct(*args)
    except Exception as msger:
        sys.stderr.write("Exception: {}\n".format(msger))
        resu = None
    return (resu)
