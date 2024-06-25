#!/usr/bin/python3
"""Square Class"""


class Square:
    """Represents a square with size and position attributes."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square with the given size and position.

        Args:
            size (int): The size of the square.
            position (tuple): The (x, y) coordinates of the square's top-left corner.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """Sets or retrieves the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """Sets retrieves the position of the square with validation."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square using # characters to stdout."""
        if self.__size == 0:
            print("")
            return

        # Handle vertical position
        for _ in range(self.__position[1]):
            print("")

        # Handle horizontal position
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
