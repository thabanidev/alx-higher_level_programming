#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


if __name__ == "__main__":
    num_of_args = len(sys.argv) - 1
    if (num_of_args != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        operator = sys.argv[2]
        b = int(sys.argv[3])
        
        if operator == '+':
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif operator == '-':
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif operator == '*':
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        elif operator == '/':
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
