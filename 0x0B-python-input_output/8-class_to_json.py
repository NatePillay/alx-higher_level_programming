#!/usr/bin/python3
"""This is a function that takes an ibject and returns the dictionary representation"""
import json


def class_to_json(obj):
    """get the ibject's attributes"""
    obj_dictv= obj.__dict__
    """create a new dictionary to store the serializable attributes"""
    json_dict = {}
    for key, value in obj_dict.items():
        """check if the attributes are serializable"""
        if isinstance (value, (list, dict, str, int, bool)):
            json_dict[key] = value
    return json_dict
