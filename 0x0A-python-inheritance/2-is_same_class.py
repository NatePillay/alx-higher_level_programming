#!/usr/bin/python3
"""checks if an object is an instance of a class"""


def is_same_class(obj, a_class):
    """Return true if object is an instance of the class, otherwise return false"""
    return obj.__class__ == a_class
