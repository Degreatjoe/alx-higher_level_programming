#!/bin/bash

# Function to send request and display size of response body
get_response_size() {
    local url="$1"
    local response_size=$(curl -sI "$url" | grep -i '^Content-Length:' | awk '{print $2}')
    
    if [[ -n "$response_size" ]]; then
        echo "$response_size"
    else
        echo "Error: Unable to retrieve content length."
    fi
}

# Main script starts here
if [[ $# -ne 1 ]]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url="$1"
get_response_size "$url"

