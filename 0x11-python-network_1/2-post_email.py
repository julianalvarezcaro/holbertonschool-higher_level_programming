#!/usr/bin/python3
"""Takes in a URL and a email
Sends a POST request with them
Displays the response
"""

if __name__ == "__main__":
    from urllib import request, parse
    import sys

    urlarg = sys.argv[1]
    email = sys.argv[2]

    data = parse.urlencode({'email': email})
    data = data.encode('ascii')

    with request.urlopen(urlarg, data) as response:
        print(response.read().decode)
