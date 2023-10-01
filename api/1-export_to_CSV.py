#!/usr/bin/python3
"""
extend your Python script to export data in the CSV format 
"""
import csv
import requests
import sys


def get_user_todos_progress(userId):
    """
    get data from an api path
    """
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(userId)
    todos_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(userId)

    try:
        response_users = requests.get(user_url)
        response_users.raise_for_status()
        users = response_users.json()
        name = users['username']

        response_todos = requests.get(todos_url)
        response_todos.raise_for_status()
        todos = response_todos.json()

        csv_file_name = '{}.csv'.format(userId)
        with open(csv_file_name, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            for todo in todos:
                csv_writer.writerow([userId, name, todo['completed'], todo['title']])
    except requests.exceptions.HTTPError as err:
        print('HTTP Error: {}'.format(err))
    except requests.exceptions.ConnectionError as err:
        print('Connection Error: {}'.format(err))
    except requests.exceptions.Timeout as err:
        print('Timeout Error: {}'.format(err))

if __name__ == "__main__":
    userId = sys.argv[1]
    get_user_todos_progress(userId)
