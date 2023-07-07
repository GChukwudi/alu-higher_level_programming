#!/usr/bin/python3
offset = -32

def uppercase(str):
    i = 0
    while i < len(str):
        if islower(str[i]):
            holder = ord(stru[i]) + offset
            new_str = chr(holder)
        else:
            new_str = str[i]
            print("{}".format(new_str), end='')
            i = i + 1
            print("")

def islower(str):
    value = ord(str)
    if value >= 97 and value <= 122:
        return True
    else:
        return False
