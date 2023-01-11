#!/usr/bin/python3
"""a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """write a string text to UTF8 and find length"""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
    return len(text)
