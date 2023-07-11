#!/usr/bin/python3
def uppercase(str):
    for a in str:
        C = ord(a) > 96 and ord(a) < 123
        print("{}".format(chr(ord(a) - 32 if C else ord(a))), end="")
    print()
