#!/usr/bin/python3
"""Fetches a URL
"""

if __name__ == "__main__":
    from urllib import request

    req = request.Request('https://intranet.hbtn.io/status')
    with request.urlopen(req) as response:
        readResp = response.read()
        print("Body response:")
        print("\t- type: " + str(type(readResp)))
        print("\t- content: " + str(readResp))
        print("\t- utf8 content: " + readResp.decode())
