#!/usr/bin/python3
"""error code"""

import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]

    r =  requests.get(url)

    if r.status_code > 400:
        print(r.text)
