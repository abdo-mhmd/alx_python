#!/usr/bin/python3
import requests, sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    status_code = response.status_code
    if status_code >= 400:
        print("Error code:", status_code)
    else:
        print("Index")