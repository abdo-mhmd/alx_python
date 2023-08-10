#!/usr/bin/python3
"""
This module contains the Base class, which serves
as the base for other classes.
"""
import requests


url = "https://alu-intranet.hbtn.io/status"
response = requests.get(url)
content = response.text
print("Body response:")
print("\t- type:", type(content))
print("\t- content:", content)