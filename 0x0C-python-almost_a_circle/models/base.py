#!/usr/bin/python3
"""test 1 test 2"""


import csv
import json
import os
import turtle


class Base:
    """represents base of all classes created"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
