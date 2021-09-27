#!/usr/bin/python3
def safe_print_list_integers(mylist=[], x=0):
    res = 0
    num = 0
    for i in mylist:
        if num >= x:
            break
        try:
            print("{:d}".format(i), end='')
        except:
            pass
        else:
            res += 1
        finally:
            num += 1
    print("")
    return res
