#!/usr/bin/python3
"""
extend your Python script to export data in the JSON format
"""
import json
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

        json_file_name = '{}.json'.format(userId)
        user_todo_list = []

        for task in todos:
            user_todo_list.append({
                'task': task['title'],
                'completed': task['completed'],
                'username': name
            })

        with open(json_file_name, mode='w') as json_file:
            json.dump({userId: user_todo_list}, json_file)
        
    except requests.exceptions.HTTPError as err:
        print('HTTP Error: {}'.format(err))
    except requests.exceptions.ConnectionError as err:
        print('Connection Error: {}'.format(err))
    except requests.exceptions.Timeout as err:
        print('Timeout Error: {}'.format(err))

if __name__ == "__main__":
    userId = sys.argv[1]
    get_user_todos_progress(userId)
