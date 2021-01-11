#!/usr/bin/python3
"""Sends a POST request
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""

    response = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    try:
        jfile = response.json()
        if jfile:
            id = jfile['id']
            name = jfile['name']
            print("[{}] {}".format(id, name))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
