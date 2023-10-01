#!/usr/bin/python3
"""
extend your Python script to export data in the JSON format
"""
import json
import requests
import sys

userID = sys.argv[1]
user_url = 'https://jsonplaceholder.typicode.com/users'
todos_url = 'https://jsonplaceholder.typicode.com/todos'

response = requests.get(todos_url)
todos = response.json()

user_name = requests.get(user_url + '/' + userID).json()['username']
json_object = {
    userID: []
}

for todo in todos:
    if todo['userId'] == int(userID):
        json_object[userID].append({
            'task': todo['title'],
            'completed': todo['completed'],
            'username': user_name
        })

with open('./{}.json'.format(userID), 'w') as js:
    json.dump(json_object, js)
