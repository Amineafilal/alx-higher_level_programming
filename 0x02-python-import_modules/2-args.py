#!/usr/bin/python3
if __name__ == "__main__":
    """ Print number of arguments """
    import sys

    num_arguments = len(sys.argv) - 1
    if num_arguments != 0:
        print("{} arguments:".format(num_arguments))
    else:
        print("0 arguments.")
    for i in range(num_arguments):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))