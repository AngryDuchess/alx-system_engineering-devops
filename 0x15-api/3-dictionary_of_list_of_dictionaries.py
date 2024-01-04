import requests
from sys import argv
import json

if __name__ == '__main__':

    users = requests.get(f'https://jsonplaceholder.typicode.com/users/').json()
    todos = requests.get(f'https://jsonplaceholder.typicode.com/todos/').json()

    def get_user_todos(id):
        return list(filter(lambda todo: todo.get('userId') == id, todos))

    def to_list(id, username):
        return list(map(lambda todo:
                        {
                            'task': todo['title'],
                            'completed': todo['completed'],
                            'username': username,
                        }, get_user_todos(id)))
    all_todo_obj = {}

    for user in users:
        id = user['id']
        username = user['username']
        all_todo_obj[id] = to_list(id, username)

    try:
        with open(f'todo_all_employees.json', 'w') as file:
            json.dump(all_todo_obj, file)
    except Exception:
        pass
