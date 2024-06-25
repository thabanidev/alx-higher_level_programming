#!/usr/bin/python3
"""Module defining a Square class."""


class Square:
    """Represents a square with a size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square.

        Args:
            size (int): The size of the square.
            position (tuple): The (x, y) coordinates of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square with validation.

        Args:
            value (tuple): The new position.

        Raises:
            TypeError: If the position is not tuple of two pos+ integers.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(i, int) and i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square."""
        return self.__size**2

    def my_print(self):
        """Prints the square with the '#' character."""
        if self.__size == 0:
            print()
            return

        [print("") for _ in range(self.__position[1])]
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Returns the string representation of the square for printing."""
        if self.__size == 0:
            return ""

        result = ["" for _ in range(self.__position[1])]
        for _ in range(self.__size):
            result.append(" " * self.__position[0] + "#" * self.__size)
        return "\n".join(result)
