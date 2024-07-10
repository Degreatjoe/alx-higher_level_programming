#!/usr/bin/python3
"""
This script fetches the 10 most recent commits of a specified GitHub repository
belonging to a specific owner, using the GitHub API.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <repository_name> <owner_name>")
        sys.exit(1)

    repo_name = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repo_name}/commits"
    params = {
        'per_page': 10,  # Number of commits to fetch
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise exception for bad responses

        commits = response.json()

        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

    except KeyError as e:
        print(f"Error parsing JSON response: {e}")
        sys.exit(1)
