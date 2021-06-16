#!/usr/bin/python3
"""
script that uses REST API to get and return data
exports data in JSON format
records all tasks from all employees
"""
import json
import requests


def export_all_to_json():
    """ saves to JSON """
    users_and_tasks = {}
    user_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = "https://jsonplaceholder.typicode.com/todos"

    user_json = requests.get(user_url).json()
    todos_json = requests.get(todo_url).json()

    user_info = {}
    for user in user_json:
        user_info[user['id']] = user['username']

    for task in todos_json:
        if users_and_tasks.get(task['userId'], False) is False:
            users_and_tasks[task['userId']] = []
        task_dict = {}
        task_dict['username'] = user_info[task['userId']]
        task_dict['task'] = task['title']
        task_dict['completed'] = task['completed']

        users_and_tasks[task['userId']].append(task_dict)

    with open("todo_all_employees.json", 'w') as jsonFile:
        json.dump(users_and_tasks, jsonFile)

if __name__ == "__main__":
    export_all_to_json()
