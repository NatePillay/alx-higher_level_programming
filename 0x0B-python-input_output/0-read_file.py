#!/usr/bin/python3
"""a function that reads text"""


def read_file(filename=""):
    """function to read the data out"""
    with open('workfile', encoding="utf-8") as f:
        read_data = f.read()
