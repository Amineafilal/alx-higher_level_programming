#!/usr/bin/python3
for x in range(97, 123):
    if chr(x) != ord('q') and chr(x) != ord('e'):
        print("{}".format(chr(x)), end="")
