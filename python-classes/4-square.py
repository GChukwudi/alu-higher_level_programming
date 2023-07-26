#!/usr/bin/python3

""" the class square calculating and displaying a square"""


class Square:
    """ Square class definition"""
    def __init__(self, size=0):
        """ constructor initialization """
        self.__size = size

    @property
    def size(self):
        """ getting size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        """ setting the size of the square """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return (self.__size ** 2)
