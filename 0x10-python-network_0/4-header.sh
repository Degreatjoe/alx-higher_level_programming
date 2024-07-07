#!/bin/bash
# Sends a GET request to the URL with a header variable and displays the response body
curl -sH "X-School-User-Id: 98" "$1"
