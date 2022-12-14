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

    def area(self):
        """
        Calculate the area of a square
        Return size ** 2
        """

        return (self.__size ** 2)
