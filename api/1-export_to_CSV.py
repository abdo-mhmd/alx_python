#!/usr/bin/python3

import csv
import requests
import sys

userID = sys.argv[1]
url = 'https://jsonplaceholder.typicode.com/users/' + userID
response = requests.get(url + '/todos')
data = response.json()

TOTAL_NUMBER_OF_TASKS = len(data)
EMPLOYEE_NAME = requests.get(url).json()['username']

with open(f'./{userID}.csv', 'w') as f:
    writer = csv.writer(f)
    for task in data:
        writer.writerow(
            [userID, EMPLOYEE_NAME, task['completed'], task['title']])
    f.close()
