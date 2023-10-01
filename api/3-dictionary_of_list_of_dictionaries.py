#!/usr/bin/python3
import json
import requests

user_url = 'https://jsonplaceholder.typicode.com/users'
todos_url = 'https://jsonplaceholder.typicode.com/todos'

users = requests.get(user_url).json()
todos = requests.get(todos_url).json()
users_count = len(users)

user = []
json_obj = {}

for userId in range(users_count):
    for todo in todos:
        if todo['userId'] == userId + 1:
            user.append({
                'username': users[userId]['username'],
                'task': todo['title'],
                'completed': todo['completed']
            })

    json_obj[userId + 1] = user
    user = []

with open('./todo_all_employees.json', 'w') as js:
    json.dump(json_obj, js)
