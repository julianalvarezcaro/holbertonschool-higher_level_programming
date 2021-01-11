#!/usr/bin/python3
"""Sends a request and displays the body of the response
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    response = requests.get(argv[1])
    code = response.status_code
    if code >= 400:
        print("Error code: " + str(code))
    else:
        print(response.text)
