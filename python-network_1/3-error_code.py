#!/usr/bin/python3
""" module uses another module to request to make
request but we deal with the header sections
but handle errors
"""
import urllib.request
import sys

"""making request to provided url"""
if __name__ == "__main__":
    """making request to provided url"""
    req = sys.argv[1]
    try:
        with urllib.request.urlopen(req) as response:
            print('Regular request')
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
