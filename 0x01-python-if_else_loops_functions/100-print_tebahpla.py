#!/usr/bin/python3
for i in range(26, 0, -1):
    print("{:c}".format(i + 64 if i % 2 else i + 96), end='')
