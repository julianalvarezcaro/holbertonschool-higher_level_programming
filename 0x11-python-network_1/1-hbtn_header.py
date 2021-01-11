#!/usr/bin/python3
"""Takes a URL and sends a request
Displays the value of X-Request-Id variable in the header
"""

if __name__ == "__main__":
    from urllib import request
    from sys import argv

    arg = argv[1]
    req = request.Request(arg)
    with request.urlopen(req) as response:
        print(response.headers.get('X-Request-Id'))
