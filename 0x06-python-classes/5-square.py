#!/usr/bin/python3
"""Defines a Square class with properties."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a square.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif int(size) < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square."""
        return self.__size**2

    @property
    def size(self):
        """Gets or sets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif int(value) < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints in stdout the square with '#'"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
