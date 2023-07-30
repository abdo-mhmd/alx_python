"""This is a sample module named my_module.

This module contains a class and a function.
"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry
"""This is a sample module named my_module.

This module contains a class and a function.
"""


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting
    from BaseGeometry.

    This class provides a concrete implementation
    of the area calculation
    for a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        area(): Calculate the area of the rectangle.
        __str__(): Return a string representation of the rectangle.

    Usage:
        # Create a Rectangle object with width 4 and height 5
        rectangle = Rectangle(4, 5)
        print(rectangle)  # Output: "[Rectangle] 4/5"
    """

    def __init__(self, width, height):
        """
        Initialize the Rectangle object with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Usage:
            # Create a Rectangle object with width 4 and height 5
            rectangle = Rectangle(4, 5)
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
        self.__dict__
