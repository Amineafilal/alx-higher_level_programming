#!/usr/bin/python3
"""Print the ASCII alphabet, in reverse order"""
c = 0
for reverse in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(reverse - c)), end="")
    if c == 0:
        c = 32
    else:
        c = 0
