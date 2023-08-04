#!/usr/bin/python3
""" documenta here """
import requests
from sys import argv


if __name__ == "__main__":
    q = argv[1] if len(argv) > 1 else ""
    try:
        re = requests.post('http://0.0.0.0:5000/search_user',
                           data={'q': q}).json()
        if 'id' in re and 'name' in re:
            print("[{}] {}".format(re['id'], re['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
