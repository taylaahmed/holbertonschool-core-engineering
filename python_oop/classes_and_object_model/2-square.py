#!/usr/bin/env python3

"""Defines an empty Square class."""


class Square:
    """Represents a square."""
    def __init__(self, size=0):
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        pass
