#!/usr/bin/python3
def search_replace(my_list, search, replace):
    mylist = list(my_list)
    for ele in range(len(mylist)):
        if mylist[ele] == search:
            mylist[ele] = replace
    return mylist
