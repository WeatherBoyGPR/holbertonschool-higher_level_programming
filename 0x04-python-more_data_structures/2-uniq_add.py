#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    if isinstance(my_list, list) and len(my_list) > 0:
        res = my_list[0]
        for x in range(len(my_list)):
            for y in range(x - 1, -1, -1):
                if my_list[x] == my_list[y]:
                    break
                if y == 0:
                    res += my_list[x]
    return res
