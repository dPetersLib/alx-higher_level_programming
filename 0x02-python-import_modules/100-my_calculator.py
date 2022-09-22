#!/usr/bin/bash
from calculator_1.py import add, sub, mul, div
import sys
if __name__ == "__main__":
    if len(sys.argv) > 3:
        a = sys.argv[1]
        p = sys.argv[2]
        b = sys.argv[3]
        if a in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] and b in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
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
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
