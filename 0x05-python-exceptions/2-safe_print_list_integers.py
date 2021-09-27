#!/usr/bin/python3
def safe_print_list_integers(mylist=[], x=0):
    res = 0
    for i in range(x):
        try:
            print("{:d}".format(mylist[i]), end='')
            res += 1
        except (ValueError, TypeError, IndexError):
            pass
    print("")
    return res
