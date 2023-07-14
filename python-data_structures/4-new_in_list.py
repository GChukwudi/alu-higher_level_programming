#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    leng = len(my_list)
    new = my_list[:]
    if 0 <= idx < leng:
        new[idx] = element
        return (new)
