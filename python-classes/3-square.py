#!/usr/bin/python3
class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): Private instance attribute
        representing the size of the square.

    Methods:
        __init__(self, size=0): Constructor method for the Square class.
        is_int(self, size): Checks if the given value
        is an integer and non-negative.
        is_negative(self, size): Checks if the given size is non-negative.
        area(self): Calculates and returns the area of the square.
        size (property): Getter method for the size attribute.
        size (setter): Setter method for the size attribute.
        my_print(self): Prints a graphical representation
        of the square using '#' characters.
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
        if size >= 0:
            return (size)
        else:
            raise ValueError("size must be >= 0")

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        self.__size = self.is_int(value)
