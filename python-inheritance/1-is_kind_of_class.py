#!/usr/bin/python3
"""This is a sample module named my_module.

This module contains a class and a function.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of,
    or if the object is an instance of a class that
    inherited from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        bool: True if the object is an instance of the
        specified class or its subclass, otherwise False.
    """
    return isinstance(obj, a_class)
