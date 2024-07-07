#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL, and displays the value
of the X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys

if sys.argv == 2:
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        header = response.read()

    print(header.get('X-Request-Id'))
