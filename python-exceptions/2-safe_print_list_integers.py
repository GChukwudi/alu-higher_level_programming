#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ret = 0
    num = 0
    while ret < x:
        try:
            print("{:d}".format(my_list[ret]), end="")
            num += 1
        except (TypeError, ValueError):
            pass
        ret += 1
    print()
    return num
