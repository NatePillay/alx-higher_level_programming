#!/usr/bin/python3
"""This is a function that takes an ibject and returns the dictionary representation"""
import json


def class_to_json(obj):
    """returns the dictionary representation of a simple data structure"""
    return obj.__dict__
