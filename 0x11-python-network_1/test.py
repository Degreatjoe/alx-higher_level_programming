#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response (decoded in utf-8).
"""

import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
email = sys.argv[2]

print(f"URL: {url}")
print(f"Email: {email}")

# Encode the data to be sent in the request
data = urllib.parse.urlencode({'email': email}).encode('utf-8')

# Create a POST request and open it
req = urllib.request.Request(url, data=data, method='POST')

try:
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print("Response Body:")
        print(body)
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code} {e.reason}")
except urllib.error.URLError as e:
    print(f"URL Error: {e.reason}")

