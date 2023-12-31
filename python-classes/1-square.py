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
        size (property): Getter method for the size attribute.
        size (setter): Setter method for the size attribute.
        area(self): Calculates and returns the area of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int, optional): The size of the square (default is 0).
        """
        self.__size = self.is_int(size)

    def is_int(self, size):
        """
        is intager asqure instance whith given size
        args:
            size (int, optional)
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
