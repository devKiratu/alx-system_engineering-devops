#!/usr/bin/python3
"""
This module uses the requests module to get information about an employee's
todo data and exports it to csv
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

        # export data to csv
        filename = "{}.csv".format(user_id)
        with open(filename, 'a', encoding='utf-8') as f:
            for todo in todos:
                line = "\"{}\",\"{}\",\"{}\",\"{}\"\n".format(
                        sys.argv[1],
                        user_data.get('username'),
                        todo.get('completed'),
                        todo.get('title'))
                f.write(line)
