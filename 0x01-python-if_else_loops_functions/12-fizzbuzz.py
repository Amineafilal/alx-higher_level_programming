#!/usr/bin/python3
def fizzbuzz():
    """Write a function that prints the numbers from 1 to 100."""
    for mod in range(1, 101):
        if mod % 3 == 0 and mod % 5 == 0:
            print("FizzBuzz ", end="")
        elif mod % 3 == 0:
            print("Fizz ", end="")
        elif mod % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(mod), end="")
