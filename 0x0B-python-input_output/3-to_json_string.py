#!/usr/bin/python3
"""a function that returns the json representation of an object"""
import json


def to_json_string(my_obj):
    """function takes single parameter"""
    return json.dumps(my_obj)

