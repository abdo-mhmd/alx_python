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


url = "http://0.0.0.0:5000/search_user"
letter = sys.argv[1] if len(sys.argv) > 1 else ""
payload = {'q': letter}
response = requests.post(url, data=payload)
try:
    json_data = response.json()
    if isinstance(json_data, dict) and 'id' in json_data and 'name' in json_data:
        print("[{}] {}".format(json_data['id'], json_data['name']))
    else:
        if json_data == {}:
            print("No result")
        else:
            print("Not a valid JSON")
except ValueError:
    print("Not a valid JSON")