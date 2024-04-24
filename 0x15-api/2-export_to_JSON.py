#!/usr/bin/python3
"""
Script that for a given employee ID,
returns information about his/her TODO list progress.
"""

import csv
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    employee_id = sys.argv[1]

    # retrieve user information
    user = requests.get(url + 'users/{}'.format(employee_id)).json()

    username = user.get("username")

    params = {"userId": employee_id}

    todos = requests.get(url + "todos", params=params).json()

    data_to_export = {employee_id: []}

    for todo in todos:
        task_info = {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username
                }
        data_to_export[employee_id].append(task_info)

    # writing json file
    with open("{}.json".format(employee_id), "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
