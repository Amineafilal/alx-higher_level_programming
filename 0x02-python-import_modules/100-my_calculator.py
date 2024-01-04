#!/usr/bin/python3
if __name__ == "__main__":
    import sys
 
    a = int(sys.argv[1])
    calllculmath = sys.argv[2]
    mathargv = len(sys.argv) - 1
    if mathargv != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if calllculmath != "+" and calllculmath != "-" and calllculmath != "*" and calllculmath != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    import calculator_1 as math
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if calllculmath == "+":
        resultmath = math.add(a, b)
    elif calllculmath == "-":
        resultmath = math.sub(a, b)
    elif calllculmath == "*":
        resultmath = math.mul(a, b)
    elif calllculmath == "/":
        resultmath = math.div(a, b)
    print("{} {} {} = {} ".format(a, calllculmath, b, resultmath)) 
