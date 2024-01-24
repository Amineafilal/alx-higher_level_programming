#!/usr/bin/python3
def magic_calculation(a, b):
    res = 0

    for x in range(0, 4):
        try:
            if x > a:
                raise Exception("To far")
            res += a ** b / x
        except ValueError:
            res += b + a
            break
    return res
