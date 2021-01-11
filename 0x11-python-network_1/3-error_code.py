#!/usr/bin/python3
"""Takes in URL
Displays body of response
Manages HTTPError exceptions
"""

if __name__ == "__main__":
    from urllib.error import HTTPError
    from urllib import request
    from sys import argv

    url = argv[1]

    try:
        req = request.Request(url)

        with request.urlopen(req) as response:
            print(response.read().decode())
    except HTTPError as error:
        print("Error code: {}".format(error.code))
