#!/usr/bin/python3
""" module uses another module to request to make request """
import urllib.request


"""making request to provided url"""
if __name__ == "__main__":
    """making request to provided url"""
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print('Body response:')
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        """ the method i used is easy way for string manipulation 
            to use a method that make use of the concept
            print out html.decode('utf-8') with string formatting
        """
        temp = str(html)
        print("\t- utf8 content: {}".format(temp[2:-1]))
