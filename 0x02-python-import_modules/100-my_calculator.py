#!/usr/bin/python3
if __name__ == "__main__":
    import sy

    a = int(sys.argv[1])
    cm = sys.argv[2]
    mathargv = len(sys.argv) - 1

    if mathargv != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if cm != "+" and cm != "-" and cm != "*" and cm != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    import calculator_1 as math

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if cm == "+":
        resultmath = math.add(a, b)
    elif cm == "-":
        resultmath = math.sub(a, b)
    elif cm == "*":
        resultmath = math.mul(a, b)
    elif cm == "/":
        resultmath = math.div(a, b)
    print("{} {} {} = {} ".format(a, cm, b, resultmath))
