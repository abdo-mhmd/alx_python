#!/usr/bin/python3
"""
This module contains the Base class, which serves
as the base for other classes.
"""
import requests


def fetch_and_display_status(url):
    """
    Fetches the status of a URL using the
    requests package and displays the content.

    Args:
        url (str): The URL to fetch.

    Returns:
        None
    """
    response = requests.get(url)
    content = response.text
    print("\t- type:", type(content))
    print("\t- content:", content)


if __name__ == '__main__':
    url = "https://alu-intranet.hbtn.io/status"
    fetch_and_display_status(url)
