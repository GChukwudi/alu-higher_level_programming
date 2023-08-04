#!/usr/bin/python3
""" module sends request
    and gets response with specific
    status code
"""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print("Regular request")
