#!/usr/bin/python3
"""Class Square that defines a square"""


class Square:

    """Private instance attribute: size"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(integer, int) for integer in value) or
                not all(integer >= 0 for integer in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    """Public instance method: that returns the current square area"""
    def area(self):
        return self.__size * self.__size

    """Public instance method that prints the square with the character #:"""
    def my_print(self):
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for x in range(self.__position[0])]
            [print("#", end="") for y in range(self.__size)]
            print()
