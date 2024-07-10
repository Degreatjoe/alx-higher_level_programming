#!/usr/bin/python3
"""
This script fetches the 10 most recent commits
of a specified GitHub repository
belonging to a specific owner, using the GitHub API.
"""
import requests
import sys

if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/\
        {repository_name}/commits"
    params = {
        'per_page': 10,  # Number of commits to fetch
    }

    response = requests.get(url, params=params)
    commits = response.json()

    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
