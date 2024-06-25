#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new square.

        Args:
            size (int or float): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation.

        Args:
            value (int or float): The new size of the square.

        Raises:
            TypeError: If the size is not a number (int or float).
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.__size**2

    def __eq__(self, other):
        """Checks if two squares have equal areas."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Checks if two squares have different areas."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Checks if this square's area is > another's."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Checks if this square's area is >= another's."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Checks if this square's area is < another's."""
        return self.area() < other.area()

    def __le__(self, other):
        """Checks if this square's area is <= to another's."""
        return self.area() <= other.area()
