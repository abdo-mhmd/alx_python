#!/usr/bin/python3
class Square:
    """A class representing a square.

    Attributes:
        __size (int): Private instance attribute
        representing the size of the square.

    Methods:
        __init__(self, size=0): Constructor method for the Square class.
        size (property): Getter method for the size attribute.
        size (setter): Setter method for the size attribute.
        area(self): Calculates and returns the area of the square.
    """
    def __init__(self, size):
        """Initializes a Square instance with a given size.

        Args:
            size (int): The size of the square.

        Usage:
            # Create a square object with a specific size
            square = Square(5)
        """
        self.__size = size
