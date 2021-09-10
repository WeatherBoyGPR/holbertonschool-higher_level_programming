#!/usr/bin/python3
def uppercase(str):
    for idx in str:
        if ord(idx) > 96 and ord(idx) < 123:
            idx = chr(ord(idx) - 32)
        print("{}".format(idx), end='')
    print("")
