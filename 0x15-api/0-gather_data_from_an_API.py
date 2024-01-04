import requests
from sys import argv

if __name__ == '__main__':

    userID = int(argv[1])

    username = requests.get(f'https://jsonplaceholder.\
            typicode.com/users/{userID}').json().get('name')
    todos = requests.get(f'https://jsonplaceholder.typicode.com/todos/').json()
    user_todos = list(filter(lambda todo: todo.get('userId') == userID, todos))
    todo_length = len(user_todos)

    completed = [todo for todo in user_todos if todo.get('completed') is True]
    no_of_completed = len(completed)

    print(f'Employee {username} is done with\
            tasks({no_of_completed}/{todo_length}):')
    for todo in user_todos:
        print(f'\t {todo.get("title")}')
