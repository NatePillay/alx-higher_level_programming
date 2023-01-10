#!/usr/bin/python3
"""check if the object is an instance of a class that is directly or indirectly from a class"""


def inherits_from(obj, a_class):
    """
    return True if object is instance of a class
    """
    return issubclass(obj.__class__, a_class)
