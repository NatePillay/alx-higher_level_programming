#!/usr/bin/python3
# square-3.py by Nathan Pillay
"""Defining a square"""


class Square:
    """ a class that represents a square"""

    def __init__(self, size=0):
        """
        initialising this square class
        Args:
            size: this is an attribute of the square
        Raises:
            TypeError for anything that is not an integer
            ValueError for size less then 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """Retrieves size of square"""

        return self.__size


    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculate area of the square
        Returns: The square of the size
        """

        return (self.__size ** 2)

    def my_print(self):
        """
        return the size of the square in #
        """
        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
