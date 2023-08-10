#!/usr/bin/python3
"""
This module contains the Base class, which serves
as the base for other classes.
"""
import requests
import sys


url = sys.argv[1]
email = sys.argv[2]
pyload = {"email": email}
response = requests.post(url, data=pyload)
try:
    json = response.json()
    if json:
        get_email = json.get("form")["email"]
        print("Your email is:", get_email)
except ValueError as e:
    print(e)
