#!/usr/bin/python3
def safe_print_integer(value):
    try:
        value_convert = '{:d}'.format(value)
        print(value_convert)
        return True
    except (ValueError, TypeError):
        return False
