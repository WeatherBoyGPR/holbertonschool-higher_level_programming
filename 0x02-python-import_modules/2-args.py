#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    idx = len(argv) - 1
    if idx != 0:
        if idx == 1:
            print("1 argument:")
        else:
            print("{} arguments:".format(idx))
        for num in range(idx):
            print("{}: {}".format(num + 1, argv[num + 1]))
            idx -= 1
    elif idx == 0:
        print("0 arguments.")
