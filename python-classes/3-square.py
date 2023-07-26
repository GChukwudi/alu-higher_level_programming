#!/usr/bin/python3
""" class square. """

class Square:
    """ defining the class square. """
    def __init__(self, size=0):
        """ defining size and validation """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ return area """
        return self.__size ** 2
