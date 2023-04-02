#!/usr/bin/python3
""" POST an emai:
    take in URL and email
    sends a POST request to URL with email as param
    display the body of the response
"""
from sys import argv
from urllib import parse
from urllib.request import Request, urlopen

if __name__ == '__main__':
    url = argv[1]

    data = parse.urlencode({'email': argv[2]}).encode('ascii')
    req = Request(url, data)
    with urlopen(req) as response:
        print(response.read().decode('utf-8'))
