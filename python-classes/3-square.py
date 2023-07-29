#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.__size = size   

    def is_int(self, size):
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
