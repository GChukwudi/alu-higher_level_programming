#!/usr/bin/python3
""" get user id
    from github
"""
import sys
import requests


url = 'https://api.github.com/user'

if __name__ == "__main__":
    res = requests.get(url, auth=(sys.argv[1], sys.argv[2])).json()
    if 'id' in res:
        print(res['id'])
    else:
        print(None)
