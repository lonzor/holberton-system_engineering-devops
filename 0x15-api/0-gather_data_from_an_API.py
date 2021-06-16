#!/usr/bin/python3
"""script that uses REST API to get and return data"""
import requests
import sys


def get_employee_tasks(empId):
    """get employee data"""
    name = ''
    task_list = []
    completed = 0

    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(empId))
    todos = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(empId))
    name = user.json().get('name')
    toJson = todos.json()

    for task in toJson:
        if task.get('completed') is True:
            completed += 1
            task_list.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, len(toJson)))
    for title in task_list:
        print("\t {}".format(title))

if __name__ == "__main__":
    get_employee_tasks(sys.argv[1])
