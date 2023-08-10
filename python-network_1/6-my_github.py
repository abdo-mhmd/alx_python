#!/usr/bin/python3
"""
This module contains the Base class, which serves
as the base for other classes.
"""
import requests
import sys


def fetch_github_user_id(username, personal_access_token):
    """
    Fetches the GitHub user ID using Basic Authentication
    with a personal access token.

    Args:
        username (str): Your GitHub username.
        personal_access_token (str): Your personal access token.

    Returns:
        int: The GitHub user ID.
    """
    url = f"https://api.github.com/users/{username}"
    headers = {
        "Authorization": f"Bearer {personal_access_token}"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data.get("id")
        return user_id
    else:
        return None


username = sys.argv[1]
personal_access_token = sys.argv[2]
user_id = fetch_github_user_id(username, personal_access_token)
print(user_id)
