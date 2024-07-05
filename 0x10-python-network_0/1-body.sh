#!/bin/bash

# Function to send GET request and display body of 200 status code response
get_url_body() {
    local url="$1"
    local response=$(curl -s -o /dev/null -w "%{http_code}" "$url")
    
    if [[ $response -eq 200 ]]; then
        curl -s "$url"
    else
        echo "Error: Received HTTP status code $response"
    fi
}

# Main script starts here
if [[ $# -ne 1 ]]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url="$1"
get_url_body "$url"

