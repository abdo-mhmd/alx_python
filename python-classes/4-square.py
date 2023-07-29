#!/usr/bin/python3
"""This is a sample module named my_module.

This module contains a class and a function.
"""


class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): Private instance attribute
        representing the size of the square.

    Methods:
        __init__(self, size=0): Constructor method for the Square class.
        is_int(self, size): Checks if the given value is an
        integer and non-negative.
        is_negative(self, size): Checks if the given size is non-negative.
        area(self): Calculates and returns the area of the square.
        size (property): Getter method for the size attribute.
        size (setter): Setter method for the size attribute.
        my_print(self): Prints a graphical representation of
        the square using '#' characters.
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int, optional): The size of the square (default is 0).
        """
        self.__size = size

    def is_int(self, size):
        """
        Checks if the given value is an integer.

        Args:
            size: The value to be checked.

        Returns:
            int: The non-negative integer value.

        Raises:
            TypeError: If the provided value is not an integer.
        """
        if isinstance(size, int):
            return (self.is_negative(size))
        else:
            raise TypeError("size must be an integer")

    def is_negative(self, size):
        """
        Checks if the given size is non-negative.

        Args:
            size: The value to be checked.

        Returns:
            int: The non-negative integer value.

        Raises:
            ValueError: If the provided value is negative.
        """
        if size >= 0:
            return (size)
        else:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size to set.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """
        self.__size = self.is_int(value)

    def my_print(self):
        """
        Print a graphical representation of the square using '#' characters.
        """
        if self.__size is 0:
            print()
        else:
            for row in range(self.__size):
                for i in range(self.__size):
                    print("#", end="")
                print("\n")
