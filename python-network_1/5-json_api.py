#!/usr/bin/python3
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    pyload = {"q": q}
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data=pyload)
    try:
        json = response.json()
        id = json.get("id")
        name = json("name")
        if id is not None and name is not None:
            print(f"[{id}] {name}")
        else:
            print("No result")
    except requests.exceptions.InvalidJSONError:
        print("Not a valid JSON")
