#!/usr/bin/python3
"""a function that appends to the end of a text file and returns chars"""


def append_write(filename="", text=""):
    """append string to end of text file"""
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
    return len(text)
