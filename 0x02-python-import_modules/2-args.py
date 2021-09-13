#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    idx = len(sys.argv) - 1
    if idx > 0:
        if idx is 1:
            print("1 argument:")
        else:
            print("{} arguments:".format(idx))
        for num in range(idx):
            print("{}: {}".format(num + 1, sys.argv[num + 1]))
            idx -= 1
    else:
        print("0 arguments.")
