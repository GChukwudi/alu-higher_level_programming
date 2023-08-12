#!/usr/bin/python3
"""
This module is composed by a function that adds two numbers
"""


def add_integer(a, b):
    """"Function that adds two integer and/or float numbers"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
