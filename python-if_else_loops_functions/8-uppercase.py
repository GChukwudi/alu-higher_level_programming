#!/usr/bin/python3
def uppercase(str):
    result = ''
    for i in str:
        result += chr(ord(i) - 32)
        print(result)
