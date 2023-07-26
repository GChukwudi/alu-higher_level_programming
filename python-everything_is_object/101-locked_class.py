#!/usr/bin/python3
""" class LockedClass with no class or object attribute """


class LockedClass:
    __slot__ = ['first_name']
