#!/usr/bin/python3
import urllib.request
import sys
"""takes in url and display the x-request-id of the
url"""


args = sys.argv[1]

with urllib.request.urlopen(args) as response:
    header = response.info()

print(header.get('X-Request-Id'))
