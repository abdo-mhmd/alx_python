"""This is a sample module named my_module.

This module contains a class and a function.
"""


class BaseGeometry:
    """
    A base class representing basic geometry operations.

    This class serves as a foundation for specific
    geometry-related classes.
    It contains the `area` method as a placeholder,
    which should be overridden in subclasses.
    It also includes the `integer_validator` method
    to validate positive integers.

    Attributes:
        None

    Methods:
        area(): Placeholder method for calculating
        the area of a geometric shape.
        integer_validator(name, value): Validates if the
        given value is a positive integer.

    Usage:
        # Create a BaseGeometry object (typically, this class
        is not directly instantiated)
        geometry = BaseGeometry()
    """
    pass

    def area(self):
        """
        Placeholder method for calculating the area of a geometric shape.

        This method is intended to be overridden in
        subclasses that inherit from BaseGeometry.
        Subclasses should provide their own implementation
        of the area calculation
        based on the specific geometric shape.

        Raises:
            Exception: Always raises an exception with
            the message "area() is not implemented".

        Usage:
            # Implement the area method in a subclass to
            calculate the area of the shape.
            class Rectangle(BaseGeometry):
                def area(self):
                    return self.__width * self.__height
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate if the given value is a positive integer.

        Args:
            name (str): The name of the value to
            be validated (for error messages).
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.

        Usage:
            # Validate if the 'width' attribute is a positive integer
            self.integer_validator('width', width)
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

        def __init_subclass__(cls):
            """
            Override the __init_subclass__ method with an empty implementation.

            This method is called when a subclass of BaseGeometry
            is created, but it's not needed in this class.
            By providing an empty implementation,
            we effectively remove it from the class.

            Usage:
            # Subclass Square will not inherit the i
            __init_subclass__ method from BaseGeometry.
            class Square(BaseGeometry):
                pass
            """
            pass
