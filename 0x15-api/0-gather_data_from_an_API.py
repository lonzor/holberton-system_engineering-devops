#!/usr/bin/python3
# script that uses REST API to get and return data
import requests
import sys

def get_employee_tasks(employeeId):
    """get employee data"""
    name = ''
    task_list = []
    completed_counter = 0

    userRes = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employeeId))
    todosRes = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(employeeId))

    name = userRes.json().get('name')
    todosJson = todosRes.json()

    for task in todosJson:
        if task.get('completed') is True:
            completed_counter += 1
            task_list.append(task.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(name, completed_counter, len(todosJson)))
    for title in task_list:
        print("\t {}".format(title))

    
    return 0

if __name__ == "__main__":
    get_employee_tasks(sys.argv[1])
