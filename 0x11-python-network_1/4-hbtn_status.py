#!/usr/bin/python3
"""Fetches a URL using requests package
"""

if __name__ == "__main__":
    import requests

    request = requests.get('https://intranet.hbtn.io/status')
    body = request.text
    print("Body response:")
    print("\t- type: " + str(type(body)))
    print("\t- content: " + body)
