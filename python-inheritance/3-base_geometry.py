"""This is a sample module named my_module.

This module contains a class and a function.
"""


class BaseGeometry:
    """
    A base class representing basic geometry operations.

    Attributes:
        None
    """
    def __init_subclass__(cls):
        """
        Override the __init_subclass__ method with an empty method.

        This will effectively remove the
        __init_subclass__ method from the class.
        """
        pass
