#!/usr/bin/python3
"""Python script takes in URL and display response
    also handle an error
"""
from sys import argv
from urllib.request import Request, urlopen
from urllib.error import HTTPError

if __name__ == '__main__':
    url = argv[1]
    req = Request(url)
    try:
        with urlopen(req) as response:
        print(response.read().decode('utf-8'))

    except HTTPError as e:
        print('Error code: {}'.format(e.code))



