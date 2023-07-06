#!/usr/bin/python3
def uppercase(str):
    for a in str:
        if ord('a') <= ord(a) <= ord('z'):
            a = chr(ord(a) - (ord('a') - ord('A')))
            print("{:s}".format(a), end='')
            print("")
