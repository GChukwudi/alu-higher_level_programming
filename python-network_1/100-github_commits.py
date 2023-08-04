#!/usr/bin/python3
""" api request
    github"""
import sys
import requests


if __name__ == "__main__":
    res = requests.get('https://api.github.com/repos/{}/{}/commits'
                       .format(sys.argv[2], sys.argv[1])).json()
    count = 0
    for commit in res:
        name = commit.get("commit").get("author").get("name")
        sha = commit.get("sha")
        print("{}: {}".format(sha, name))
        count += 1
        if count == 10:
            break
