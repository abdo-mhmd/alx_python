#!/usr/bin/python3
"""
extend your Python script to export data in the JSON format
"""
import json
import requests
import sys

def get_Json(userId):
    url = 'https://jsonplaceholder.typicode.com/users/' + userId
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
        json_obj[userId].append(task_obj)
        task_obj = {}
        i += 1

    return json_obj


userID = sys.argv[1]
with open(f'./{userID}.json', 'w') as f:
    json_obj = get_Json(userID)
    json.dump(json_obj, f)
    f.close()
