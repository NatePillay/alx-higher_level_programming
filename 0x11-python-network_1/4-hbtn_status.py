#!/usr/bin/python3
"""  fetches https://alx-intranet.hbtn.io/status """

if __name__ == "__main__":
    from urllib.request import urlopen, Request

    url = "https://alx-intranet.hbtn.io/status"
    req = Request(url)
    with urlopen(req) as res:
        content = res.read()

    print("Body response:")
    print('\t- type:', type(response.content))
    print('\t- content:', response.content.decode('utf-8'))
