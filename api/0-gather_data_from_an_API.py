#!/usr/bin/python3
import requests
import sys

userID = sys.argv[1]
url = 'https://jsonplaceholder.typicode.com/users/'
response = requests.get(url + str(userID) + '/todos')
data = response.json()

TOTAL_NUMBER_OF_TASKS = len(data)
NUMBER_OF_DONE_TASKS = 0
EMPLOYEE_NAME = requests.get(url + str(userID)).json()['name']
tasks = []

for todo in data:
    if todo.get('completed') == True:
        NUMBER_OF_DONE_TASKS += 1
        tasks.append(todo.get('title'))

print('Employee {} is done with tasks({}/{})'.format(EMPLOYEE_NAME,
      NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

for task in tasks:
    print('\t' + task)

