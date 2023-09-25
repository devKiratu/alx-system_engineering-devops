#!/usr/bin/python3
"""
This module uses the requests module to get information about an employee's
todo data
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        user_url = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"
        res = requests.get(user_url)
        user_data = res.json()
        user_name = user_data.get("name")

        todos_url = "https://jsonplaceholder.typicode.com/todos"
        res = requests.get(todos_url, params={'userId': sys.argv[1]})
        todos = res.json()
        completed_todos = list(filter(
            lambda todo: todo.get("completed"), todos))
        output = "Employee {} is done with tasks({}/{})".format(
                user_name, len(completed_todos), len(todos)
                )
        print(output)
        for todo in completed_todos:
            print("\t {}".format(todo.get("title")))

        # export data to csv
        filename = "{}.csv".format(sys.argv[1])
        with open(filename, 'a', encoding='utf-8') as f:
            for todo in todos:
                line = "\"{}\",\"{}\",\"{}\",\"{}\"\n".format(
                        sys.argv[1],
                        user_data.get('username'),
                        todo.get('completed'),
                        todo.get('title'))
                f.write(line)
