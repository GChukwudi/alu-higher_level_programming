#!/usr/bin/python3
offset = -32

def uppercase(stru):
    i = 0
    while i < len(stru):
        if islower(stru[i]):
            holder = ord(stru[i]) + offset
            new_str = chr(holder)
        else:
            new_str = stru[i]
            print("{}".format(new_str), end='')
            i = i + 1
            print("")

def islower(strs):
    value = ord(strs)
    if value >= 97 and value <= 122:
        return True
    else:
        return False
