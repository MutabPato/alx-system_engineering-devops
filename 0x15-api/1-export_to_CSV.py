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

    # check if ID is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # retrieve user information
    user_response = requests.get(url + 'users/{}'.format(employee_id))
    user = user_response.json()

    # retrieve username
    username = user.get("username")

    # retrieve Todo list for the employee
    params = {"userId": employee_id}
    todos_response = requests.get(url + "todos", params=params)
    todos = todos_response.json()

    # writing csv file
    with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for todo in todos:
            writer.writerow([employee_id, username, todo.get(
                "completed"), todo.get("title")])
