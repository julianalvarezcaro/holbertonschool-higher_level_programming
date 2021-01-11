#!/usr/bin/python3
"""Sends a POST request
Displays body of the response
"""

if __name__ == "__main__":
    from sys import argv
    import requests

    response = requests.post(argv[1], data={'email': argv[2]})
    print(response.text)
