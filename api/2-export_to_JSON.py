#!/usr/bin/python3
import json
import requests
import sys

userID = sys.argv[1]
url = 'https://jsonplaceholder.typicode.com/users/' + userID
response = requests.get(url + '/todos')
data = response.json()

TOTAL_NUMBER_OF_TASKS = len(data)
EMPLOYEE_NAME = requests.get(url).json()['username']

task_obj = {}
json_obj = {
    userID: []
}

i = 0

while i < len(data):
    task_obj['task'] = data[i]['title']
    task_obj['completed'] = data[i]['completed']
    task_obj['username'] = EMPLOYEE_NAME
    json_obj[userID].append(task_obj)
    task_obj = {}
    i += 1

with open(f'./{userID}.json', 'w') as f:
    json.dump(json_obj, f)
    f.close()
