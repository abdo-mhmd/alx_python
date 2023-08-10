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
email = sys.argv[2]
pyload = {"email": email}
response = requests.post(url, data=pyload)
try:
    json = response.json().get("form")
    if json:
        get_email = json.get("email")
        print("Email:", get_email)
except ValueError as e:
    print(e)
