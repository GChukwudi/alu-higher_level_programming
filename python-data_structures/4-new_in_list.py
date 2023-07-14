#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        new_lt = my_list[:]
        return new_lt
    elif idx >= len(my_list):
        new_l = my_list[:]
        return new_l
    else:
        new_2 = my_list[:]
        new_2[idx] = element
        return new_2
