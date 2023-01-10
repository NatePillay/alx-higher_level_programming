#!/bin/usr/python3
"""function to check if object is instance of a class or obj from inherited class"""


def is_kind_of_class(obj, a_class):
    """Retrun true if object is an instance of the class, otherwise false"""
    return isinstance(obj, a_class)
