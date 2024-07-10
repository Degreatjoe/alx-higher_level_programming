#!/usr/bin/python3
"""
This script takes GitHub credentials (username and personal access token)
and uses the GitHub API to display your GitHub user ID.
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]  # This should be your personal access token

    url = f"https://api.github.com/user"
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        user_data = response.json()
        print(user_data['id'])
    else:
        print("None")
