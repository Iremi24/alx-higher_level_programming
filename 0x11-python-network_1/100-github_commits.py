#!/usr/bin/python3
"""
A Python script that lists 10 commits (from the most recent to oldest) of a specified repository by a given user
"""

import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'
    try:
        response = requests.get(url)
        data = response.json()
        for commit in data[:10]:  # Get the 10 most recent commits
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    except Exception as e:
        print(f"An error occurred: {e}")
