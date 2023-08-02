"""This is a sample module named my_module.

This module contains a class and a function.
"""


class BaseGeometry:
    """
    A base class representing basic geometry operations.

    Attributes:
        None
    """

    def __dir__(cls):
        """
        Override the dir() method to exclude
        '__init_subclass__' from the list of attributes.

        This method is called when using the dir()
        function on an instance of BaseGeometry.
        It returns a custom list of attributes without
        including '__init_subclass__'.

        Returns:
            List[str]: A list of strings containing
            the names of the instance attributes.

        Usage:
            # When calling dir() on an instance of BaseGeometry,
            '__init_subclass__' will not be included.
            bg = BaseGeometry()
            dir(bg)
        """
        attributes = super().__dir__()
        return [attr for attr in attributes if attr != '__init_subclass__']
