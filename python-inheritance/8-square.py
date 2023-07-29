#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

class Square(Rectangle):

    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", self.__size)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return "[{}] {}/{}".format(__class__.__name__, self.__size, self.__size)
