#!/usr/bin/python3
def no_c(my_string):
    no_c = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(no_c))
