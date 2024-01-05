#!/usr/bin/python3
"""stores data as json"""
import json
import requests
from sys import argv


if __name__ == '__main__':

    userID = int(argv[1])

    username = requests.get(f'https://jsonplaceholder.\
            typicode.com/users/{userID}').json().get('username')
    todos = requests.get(f'https://jsonplaceholder.typicode.com/todos/').json()
    user_todos = list(filter(lambda todo: todo.get('userId') == userID, todos))

    to_json = {userID: list(map(lambda todo: {'task': todo['title'],
                                              'completed': todo['completed'],
                                              'username': username, },
                                user_todos))}

    try:
        with open(f'{userID}.json', 'w') as file:
            json.dump(to_json, file)
    except Exception:
        pass
