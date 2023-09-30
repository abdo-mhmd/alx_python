import json
import requests

url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)

if response is not None:
    data = response.json()
    users_len = len(data)
    task_obj = {}
    json_obj = {}
    list_todo = []


    for i in range(users_len):
        userID = data[i]['id']
        userName = data[i]['username']
        
        url_todo = url + '/' + str(userID) + '/todos'
        response_todo = requests.get(url_todo)
        data_todo = response_todo.json()

        for task in data_todo:
            task_obj['username'] = userName
            task_obj['task'] = task['title']
            task_obj['completed'] = task['completed']
            list_todo.append(task_obj)
            task_obj = {}

        json_obj[userID] = list_todo
        list_todo = []

    with open('./todo_all_employees.json', 'w') as f:
        json.dump(json_obj, f)
else:
    print('Error')