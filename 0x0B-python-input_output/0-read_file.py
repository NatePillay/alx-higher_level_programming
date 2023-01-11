#!/usr/bin/python3
"""a function that reads text"""


def read_file(filename=""):
    """function to print the text of UTF-8"""
    with open('workfile', encoding="utf-8") as f:
        print(f.read(), end="")
