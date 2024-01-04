#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num_arguments = len(sys.argv) - 1
    totaladd = 0
    for i in range(num_arguments):
        sumadd = int(sys.argv[i + 1])
        totaladd += sumadd
    print("{}".format(totaladd))
