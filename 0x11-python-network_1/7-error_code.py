#!/usr/bin/python3
"""error code"""

import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]

    r =  requests.post(url)

    if r.status_code >= 400:
        print(f"Error code: {r.status_code}")
