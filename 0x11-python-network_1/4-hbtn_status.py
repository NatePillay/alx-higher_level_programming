#!/usr/bin/python3
"""  fetches https://alx-intranet.hbtn.io/status """

if __name__ == "__main__":
    from requests import get

    url = "https://alx-intranet.hbtn.io/status"
    req = get(url)
    print("Body response:")
    print('\t- type:', type(req.text))
    print('\t- content:', req.text)
