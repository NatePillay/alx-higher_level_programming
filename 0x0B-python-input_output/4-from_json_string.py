#!/usr/bin/python3
"""a function that returns a python data structure"""
import json


def from_json_string(my_str):
    """Returnes the json representation of a string object"""
    return json.loads(my_str)
