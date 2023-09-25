#!/usr/bin/python3
"""
This module uses the requests module to get all employees and all their todos
data and exports them to json
"""
import json
import requests
import sys


if __name__ == "__main__":
    user_url = f"https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users = requests.get(user_url).json()
    all_objs = {}
    for user in users:
        user_id = user.get('id')
        todos = requests.get(todos_url, params={'userId': user_id}).json()
        formatted_todos = []
        for todo in todos:
            obj = {}
            obj['username'] = user.get('username')
            obj['task'] = todo.get('title')
            obj['completed'] = todo.get('completed')
            formatted_todos.append(obj)
        all_objs[user_id] = formatted_todos

    filename = "todo_all_employees.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(all_objs, f)
