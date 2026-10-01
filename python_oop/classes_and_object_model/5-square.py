#!/usr/bin/env python3

"""Defines an empty Square class."""


class Square:
    """Represents a square."""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Return size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size of square"""
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return square area"""
        return self.__size * self.__size

    def my_print(self):
        """Print square"""
        i = 0
        while i < self.__size:
            n = 0
            while n < self.__size:
                print(f"#", end="")
                n += 1
            print("")
            i += 1
        if self.__size == 0:
            print("")
