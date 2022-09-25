#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    if len(sys.argv) > 3:
        try:
            a = int(sys.argv[1])
            opr = str(sys.argv[2])
            b = int(sys.argv[3])
        except ValueError:
            print(f"Usage: {sys.argv[0]} <a> <operator> <b>")
            (sys.exit(1))
        if opr == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
            sys.exit(0)
        elif opr == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
            sys.exit(0)
        elif opr == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
            sys.exit(0)
        elif opr == '/':
            print("{} / {} = {}".format(a, b, div(a, b)))
            sys.exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
    else:
        print(f"Usage: {sys.argv[0]} <a> <operator> <b>")
        (sys.exit(1))