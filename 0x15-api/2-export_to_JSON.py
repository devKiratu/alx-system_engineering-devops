#!/usr/bin/python3
"""
This module uses the requests module to get information about an employee's
todo data
"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        user_id = sys.argv[1]
        user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
        res = requests.get(user_url)
        user_data = res.json()
        user_name = user_data.get("name")

        todos_url = "https://jsonplaceholder.typicode.com/todos"
        res = requests.get(todos_url, params={'userId': sys.argv[1]})
        todos = res.json()
        completed_todos = list(filter(
            lambda todo: todo.get("completed"), todos))
        output = "Employee {} is done with tasks({}/{}):".format(
                user_name, len(completed_todos), len(todos)
                )
        print(output)
        for todo in completed_todos:
            print("\t {}".format(todo.get("title")))

        # export json data
        jsonfile = "{}.json".format(user_id)
        user_obj = {}
        formatted_todos = []
        for todo in todos:
            obj = {}
            obj["task"] = "{}".format(todo.get('title'))
            obj["completed"] = todo.get('completed')
            obj["username"] = "{}".format(user_data.get('username'))
            formatted_todos.append(obj)
        user_obj[user_id] = formatted_todos
        with open(jsonfile, 'w', encoding='utf-8') as f:
            json.dump(user_obj, f)
