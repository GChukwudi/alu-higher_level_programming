#!/usr/bin/python3
""" module uses another module to request to make
request but we deal with the header sections
"""
import urllib.request
import sys

"""making request to provided url"""
if __name__ == "__main__":
    """making request to provided url"""
    req = sys.argv[1]
    with urllib.request.urlopen(req) as response:
        print(response.headers.get('X-Request-Id'))
