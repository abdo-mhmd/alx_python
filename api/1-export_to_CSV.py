#!/usr/bin/python3
"""
extend your Python script to export data in the CSV format 
"""
import csv
import requests
import sys

userID = sys.argv[1]
user_url = 'https://jsonplaceholder.typicode.com/users'
todos_url = 'https://jsonplaceholder.typicode.com/todos'

response = requests.get(todos_url)
todos = response.json()

user_name = requests.get(user_url + '/' + userID).json()['username']

with open('{}.csv'.format(userID), 'w') as f:
    writer = csv.writer(f)
    for todo in todos:
        if todo['userId'] == int(userID):
            writer.writerow([userID, user_name, todo['completed'], todo['title']])
