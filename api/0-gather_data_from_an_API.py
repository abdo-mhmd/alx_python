#!/usr/bin/python3
"""
get data from an api path
"""
import requests
import sys

def get_user_todos(userId):
    """
    get data from an api path
    """
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(userId)
    todos_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(userId)

    try:
        response_users = requests.get(user_url)
        response_users.raise_for_status()
        users = response_users.json()
        name = users['name']

        response_todos = requests.get(todos_url)
        response_todos.raise_for_status()
        todos = response_todos.json()

        completed_tasks = [task for task in todos if task['completed']]

        todos_count = len(todos)
        completed_tasks_count = len(completed_tasks)

        print('Employee {} is done with tasks({}/{}):'.format(name, completed_tasks_count, todos_count))
        for task in completed_tasks:
            print('\t {}'.format(task['title']))

    except requests.exceptions.HTTPError as err:
        print('HTTP Error: {}'.format(err))
    except requests.exceptions.ConnectionError as err:
        print('Connection Error: {}'.format(err))
    except requests.exceptions.Timeout as err:
        print('Timeout Error: {}'.format(err))

if __name__ == "__main__":
    userId = sys.argv[1]
    get_user_todos(userId)
