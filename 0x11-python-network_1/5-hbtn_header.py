#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""
from sys import argv
from requests import get

if __name__ == "__main__":
    print(get(argv[1]).headers.get("X-Request-Id"))
