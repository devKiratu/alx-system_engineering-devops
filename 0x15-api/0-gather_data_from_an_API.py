#!/usr/bin/python3
"""
This module uses the requests module to get information about an employee's
todo data
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        user_id = sys.argv[1]
        user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
        user_data = requests.get(user_url).json()

        todos_url = "https://jsonplaceholder.typicode.com/todos"
        todos = requests.get(todos_url, params={'userId': user_id}).json()

        completed_todos = list(filter(
            lambda todo: todo.get("completed"), todos))

        output = "Employee {} is done with tasks({}/{}):".format(
                user_data.get("name"), len(completed_todos), len(todos)
                )
        print(output)
        for todo in completed_todos:
            print("\t {}".format(todo.get("title")))
