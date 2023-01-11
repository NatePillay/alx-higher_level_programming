#!/usr/bin/python3
"""write a function that writes an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    json_store = json.dumps(my_obj)
    with open(filename,'w') as f:
        f.write(json_str)
