#!/usr/bin/python3
"""stores data as csv"""
import csv
import requests
from sys import argv


if __name__ == '__main__':

    userID = int(argv[1])

    username = requests.get(f'https://jsonplaceholder.\
            typicode.com/users/{userID}').json().get('name')
    todos = requests.get(f'https://jsonplaceholder.typicode.com/todos/').json()
    user_todos = list(filter(lambda todo: todo.get('userId') == userID, todos))

    to_csv = list(map(lambda todo: [str(userID), username,
                  str(todo.get('completed')), todo.get('title')], user_todos))

    try:
        with open(f'{userID}.csv', 'w') as file:
            csv_file = csv.writer(file, quoting=csv.QUOTE_ALL)
            csv_file.writerows(to_csv)
    except Exception:
        pass
