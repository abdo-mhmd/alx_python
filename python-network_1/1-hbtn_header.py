#!/usr/bin/python3
"""
This module contains the Base class, which serves
as the base for other classes.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    try:
        header = response.headers
        if header:
            request_id = header.get("X-Request-Id")
            print(request_id)
    except ValueError as e:
        print(e)
