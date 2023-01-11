#!/usr/bin/python3
"""we are inheriting here"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class we are using is a square"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
