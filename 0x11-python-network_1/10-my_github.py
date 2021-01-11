#!/usr/bin/python3
"""Displays my GitHub id
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    user = argv[1]
    passw = argv[2]

    response = requests.get('https://api.github.com/user', auth=(user, passw))
    jfile = response.json()
    print(jfile.get('id'))
