#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for string in my_list:
        if i >= x:
            break
        try:
            print("{}".format(string), end='')
        except TypeError:
            print("something about a non-empty format string")
        i += 1
    print("")
    return i
