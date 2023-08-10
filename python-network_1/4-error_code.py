#!/usr/bin/python3
"""
This module contains the Base class, which serves
as the base for other classes.
"""
import requests
import sys

"""
This module contains the Base class, which serves
as the base for other classes.
"""


url = sys.argv[1]

response = requests.get(url)
content = response.text
if response.status_code >= 400:
    print(f"Error code: {response.status_code}")
else:
    print("Regular request")
