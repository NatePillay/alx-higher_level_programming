#!/usr/bin/python3
""" checks if object is an instance of a class that
inherited from the specified class or not
"""


class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")
