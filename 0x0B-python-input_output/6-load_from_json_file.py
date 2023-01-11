#!/usr/bin/python3
"""This module defines a JSON file-writing function"""
import json


def load_from_json_file(filename):
   """we want to load the filw"""
   with open(filename) as f:
       return json.load(f)
