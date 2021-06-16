#!/usr/bin/python3
"""
script that uses REST API to get and return data
exports data in CSV format
"""
import csv
import requests
import sys


def save_to_csv(empId):
    """ saves to CSV """
    name = ''
    all_tasks = []

    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(empId))
    todos = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(empId))
    name = user.json().get('username')
    toJson = todos.json()

    for task in toJson:
        t_row = []
        t_row.append(empId)
        t_row.append(name)
        t_row.append(task.get("completed"))
        t_row.append(task.get("title"))
        all_tasks.append(t_row)

    with open("{}.csv".format(empId), 'w') as csvFile:
        csvwriter = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        csvwriter.writerows(all_tasks)

if __name__ == "__main__":
    save_to_csv(sys.argv[1])
