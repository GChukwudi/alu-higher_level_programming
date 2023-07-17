#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    for a in set(my_list):
        add += a
    return add
