#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """this represent a rectangle"""
    def __init__(self, height, width):
        """initializing this rectangle class
        Args:
            width:
            height:
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """retrieves height attribute"""
        return self._height

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        """retrieves width attribute"""
        return self._width

    @width.setter
    def width(self, value):
        """sets width attributes"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")