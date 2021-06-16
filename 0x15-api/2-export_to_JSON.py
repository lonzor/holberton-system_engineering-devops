#!/usr/bin/python3
"""
script that uses REST API to get and return data
exports data in JSON format
"""
import json
import requests
import sys


def save_to_json(empId):
    """ saves to JSON """
    name = ''
    user_dict = {}

    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(empId))
    todos = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(empId))
    name = user.json().get('username')
    toJson = todos.json()

    user_dict[empId] = []

    for task in toJson:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["username"] = name
        task_dict["completed"] = task.get('completed')

        user_dict[empId].append(task_dict)

    with open("{}.json".format(empId), 'w') as jsonFile:
        json.dump(user_dict, jsonFile)

if __name__ == "__main__":
    save_to_json(sys.argv[1])
