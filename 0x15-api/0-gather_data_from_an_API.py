#!/usr/bin/python3
"""
Script that for a given employee ID, returns information about his/her TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'

    # check if ID is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # retrieve user information
    user_response = requests.get(url + 'users/{}'.format(employee_id))
    user = user_response.json()
    
    # retrieve Todo list for the employee
    params = {"userId": employee_id}
    todos_response = request.get(url + "todos", params=params)
    todos = todos_response.json()

    completed = []
    
    # filter completed tasks
    for todo in todos:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))
    
    #  display progress information
    print("Employee {} is done with tasks({}/{})".format(user.get("name").
        len(completed).len(todos)))
    
    # display titles of completed tasks
    for complete in completed:
        print("\t {}".format(complete))
