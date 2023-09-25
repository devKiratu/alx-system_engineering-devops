#!/usr/bin/python3
"""
This module uses the requests module to get information about an employee's
todo data and exports it to a json file
"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        user_id = sys.argv[1]
        user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
        user_data = requests.get(user_url).json()

        todos_url = "https://jsonplaceholder.typicode.com/todos"
        todos = requests.get(todos_url, params={'userId': user_id}).json()

        # export json data
        jsonfile = "{}.json".format(user_id)
        user_obj = {}
        formatted_todos = []
        for todo in todos:
            obj = {}
            obj["task"] = todo.get('title')
            obj["completed"] = todo.get('completed')
            obj["username"] = user_data.get('username')
            formatted_todos.append(obj)
        user_obj[user_id] = formatted_todos
        with open(jsonfile, 'w', encoding='utf-8') as f:
            json.dump(user_obj, f)
