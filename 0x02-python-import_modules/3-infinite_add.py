#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    res = int(0)
    if len(argv) > 1:
        for num in range(1, len(argv)):
            res += int(argv[num])
print("{:d}".format(res))
