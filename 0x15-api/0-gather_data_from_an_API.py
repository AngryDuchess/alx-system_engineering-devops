#!/usr/bin/python3
"""gets employee data ffrom api given"""
import requests
from sys import argv

if __name__ == '__main__':

    userID = int(argv[1])
    url = f'https://jsonplaceholder.typicode.com/users/{userID}'

    EMPLOYEE_NAME = requests.get(url).json().get('name')
    all_todos = requests.get(
        f'https://jsonplaceholder.typicode.com/todos/').json()
    user_todos = list(
        filter(lambda todo: todo.get('userId') == userID, all_todos))
    TOTAL_NUMBER_OF_TASKS = len(user_todos)

    completed = [todo for todo in user_todos if todo.get('completed') is True]
    NUMBER_OF_DONE_TASKS = len(completed)

    first_line = f'Employee {EMPLOYEE_NAME} is done with '
    print(first_line +
          f'tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):')
    for todo in user_todos:
        print(f'\t {todo.get("title")}')
