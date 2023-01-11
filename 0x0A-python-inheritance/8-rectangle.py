#!/usr/bin/python3
"""Inherit from baseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class to define rectangle using base geometry"""
    
    def __init__(self, width, height):
        """define the characteristics"""
        self.integer_validator("width",width)
        self.__width = width
        self.integer_validator("height",height)
        self.__height = height
        
