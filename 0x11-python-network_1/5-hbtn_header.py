#!/usr/bin/python3
"""Sends a request
Displays the value of the X-Request-Id variable
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    request = requests.get(argv[1])
    req_id = request.headers.get('X-Request-Id')
    print(req_id)
