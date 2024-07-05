#!/usr/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Retrieve the URL and get the size of the response body in bytes
response_size=$(curl -sI "$1" | grep -i 'Content-Length' | awk '{print $2}' | tr -d '\r')

# Print the size of the response body
echo "$response_size"

