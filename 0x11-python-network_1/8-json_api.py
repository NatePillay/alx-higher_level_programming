#!/usr/bin/python3
"""script using request library for web servers"""

if __name__ == "__main__":
    from sys import argv
    from requests import post

    url = "http://0.0.0.0:5000/search_user"
    if len(argv) > 1:
        q = argv[1]
    else:
        q = " "

    response = post(url, data={"q": q})

    try:
        res_json = response.json()
        if res_json == {}:
            print("No result")
        else:
            print(f'[{res_json.get("id")}] {res_json.get("name")}')
    except ValueError:
        print("Not a valid JSON")
