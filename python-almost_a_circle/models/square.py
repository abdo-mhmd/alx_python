from models.rectangle import Rectangle
"""
The Rectangle class represents a rectangle with
width, height, position (x, y), and an identifier.
"""


class Square(Rectangle):
    """
    This class represents a square, inheriting from the Rectangle class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate position. Defaults to 0.
            y (int, optional): The y-coordinate position. Defaults to 0.
            id (int, optional): The unique identifier. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square, updating both width and height.

        Args:
            value (int): The new size of the square.

        Raises:
            ValueError: If the value is not greater than 0.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Get a string representation of the square.

        Returns:
            str: The formatted string containing the
            class name, id, position, and size.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
