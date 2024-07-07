#!/usr/bin/python3
"""takes in url and display the x-request-id of the
url"""
import urllib.request
import sys


args = sys.argv[1]

with urllib.request.urlopen(args) as response:
    header = response.info()

print(header.get('X-Request-Id'))
