#!/usr/bin/python3
"""Python script takes in URL and display response
    also handle an error
"""
from sys import argv
from urllib.request import urlopen
from urllib.error import HTTPError

if __name__ == '__main__':
    try:
        with urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))

    except HTTPError as e:
        print('Error code: {}'.format(e.code))
