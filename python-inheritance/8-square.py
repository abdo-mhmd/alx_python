#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle
"""This is a sample module named my_module.

This module contains a class and a function.
"""


class Square(Rectangle):
    """
    A class representing a square, inheriting from Rectangle.

    This class provides a concrete implementation
    of the area calculation for a square.

    Attributes:
        size (int): The size of the square (width and height are equal).

    Methods:
        area(): Calculate the area of the square.
        __str__(): Return a string representation of the square.

    Usage:
        # Create a Square object with size 4
        square = Square(4)
        print(square)  # Output: "[Square] 4/4"
    """
    def __init__(self, size):
        """
        Initialize the Square object with size.

        Args:
            size (int): The size of the square (width and height are equal).

        Usage:
            # Create a Square object with size 4
            square = Square(4)
        """
        self.__size = size
        self.integer_validator("size", self.__size)

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.

        Usage:
            # Calculate the area of the square object 'square'
            area = square.area()
        """
        return self.__size ** 2

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A string representing the square
            in the format "[Square] size/size".

        Usage:
            # Get the string representation of the square object 'square'
            str_representation = str(square)
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
