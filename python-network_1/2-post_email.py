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

data = {'email': email}
response = requests.post(url, data=data)

print(response.text)
