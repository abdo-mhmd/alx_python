#!/usr/bin/python3
"""
This module contains the Base class, which serves
as the base for other classes.
"""


class Base:
    """
    The Base class serves as a base class for other classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base instance.

        Args:
            id (int, optional): The unique identifier. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
