#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    if argv[2] is '+':
        res = add(int(argv[1]), int(argv[3]))
    elif argv[2] is '*':
        res = mul(int(argv[1]), int(argv[3]))
    elif argv[2] is '-':
        res = sub(int(argv[1]), int(argv[3]))
    elif argv[2] is '/':
        res = div(int(argv[1]), int(argv[3]))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(argv[1], argv[2], argv[3], res))
