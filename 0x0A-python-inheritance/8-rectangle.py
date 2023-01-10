#!/usr/bin/python3
"""create a rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """we define an init method"""

    def __init__(self, width, height):
        """including our weight and height attribute"""
        self.__width = width
        self.__height = height
        integer_validator("width",width)
        integer_validator("height",height)
