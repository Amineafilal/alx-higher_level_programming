#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

numberlast = abs(number) % 10

if number < 0:
    numberlast = -numberlast
print("Last digit of {} is {} and is ".format(number, numberlast), end="")
if numberlast > 5:
    print("greater than 5 and not 0")
elif numberlast == 0:
    print("0")
els:
    print("less than 6 and not 0")
