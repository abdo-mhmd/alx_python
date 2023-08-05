"""
This module contains the Base class,
which serves as the base for other classes.
"""
from models.base import Base
"""
This module contains the Base class,
which serves as the base for other classes.
"""


class Rectangle(Base):
    """
    The Rectangle class represents a rectangle with width,
    height, position (x, y), and an identifier.
    It inherits from the Base class.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate position. Defaults to 0.
            y (int, optional): The y-coordinate position. Defaults to 0.
            id (int, optional): The unique identifier. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The calculated area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Display the rectangle using '#' characters in stdout.

        The rectangle is printed with respect to its position (x, y).
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Get a formatted string representation of the rectangle.

        Returns:
            str: The formatted string containing the class name,
            id, position, width, and height.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """
        Update attributes of the Rectangle instance
        using positional or keyword arguments.

        Args:
            *args: Positional arguments. Can be used for id,
            width, height, x, and y.
            **kwargs: Keyword arguments. Key-value pairs
            to update attributes.

        Raises:
            ValueError: If arguments are not valid
            for the attributes.
        """
        if args:
            num_args = len(args)
            if num_args > 0:
                self.id = args[0]
            if num_args > 1:
                self.width = args[1]
            if num_args > 2:
                self.height = args[2]
            if num_args > 3:
                self.x = args[3]
            if num_args > 4:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
