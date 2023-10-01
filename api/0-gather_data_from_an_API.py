#!/usr/bin/python3
"""
get data from an api path
"""
import requests
import sys

userID = sys.argv[1]
user_url = 'https://jsonplaceholder.typicode.com/users'
todos_url = 'https://jsonplaceholder.typicode.com/todos'
response = requests.get(todos_url)
todos = response.json()
todos_count = 0
todos_done = 0
name = requests.get(user_url + '/' + str(userID)).json()['name']
tasks = []
      
for todo in todos:
    if todo['userId'] == int(userID):
        todos_count += 1
        if todo['completed'] is True:
            todos_done += 1
            tasks.append(todo['title'])

print('Employee {} is done with tasks({}/{})'.format(name, todos_done, todos_count))

for task in tasks:
    print('\t' + task)
    