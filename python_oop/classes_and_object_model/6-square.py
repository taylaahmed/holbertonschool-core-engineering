#!/usr/bin/env python3

"""Defines an empty Square class."""


class Square:
    """Represents a square."""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Return size"""
        return self.__size

    @property
    def position(self):
        """Return position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of square"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__size):
            print(" " * self.__position[0] +
                  "#" * self.__size)


    def __str__(self):
        """Return the printable representation of the square."""
        if self.__size == 0:
            return ""

        lines = []
        for _ in range(self.__size):
            lines.append(" " * self.__position[0] +
                         "#" * self.__size)

        return "\n".join(lines) + "\n"
