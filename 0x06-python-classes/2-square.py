#!/usr/bin/python3
"""Defines a Square class with size validation."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a square.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        if int(size) < 0:
            raise ValueError("Square size must be >= 0")
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.__size = size
