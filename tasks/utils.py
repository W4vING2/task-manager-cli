import json
from json import JSONDecodeError
from tasks.decors import *

@log
def add_task(name:str, description:str) -> None:
    tasks = load_tasks()
    new_id = generate_id(tasks)
    with open('db.json', 'w') as f:
       tasks.append({'name':name, 'description':description, 'id': new_id, 'is_completed':False})
       json.dump(tasks, f, indent=4)
    print(f"Task {new_id} added.")

@log
def generate_id(tasks: list) -> int:
    if len(tasks) == 0:
        return 1
    else:
        count = 1
        for i in tasks:
            if i['id'] > count:
                count = i['id']
        return count + 1

@log
def load_tasks() -> list:
    try:
        with open('db.json', 'r') as file:
            data = json.load(file)
            if not isinstance(data, list):
                return []
            return data
    except (JSONDecodeError, FileNotFoundError):
        return []

@log
@validate_id
def delete_task(task_id: int) -> None:
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task['id'] != task_id]
    if len(new_tasks) == len(tasks):
        print('Task not found')
    else:
        print(f'Task {task_id} deleted.')
        with open('db.json', 'w') as file:
            json.dump(new_tasks, file, indent=4)

@log
@validate_id
def update_task(task_id: int, new_name: str = None, new_description: str = None, is_completed: str = False) -> None:
    tasks = load_tasks()
    found = False
    completed = False
    if is_completed == 'y':
        completed = True
    for task in tasks:
        if task['id'] == task_id:
            if new_name:
                task['name'] = new_name
            if new_description:
                task['description'] = new_description
            if is_completed:
                task['is_completed'] = completed
            found = True
            break
    if not found:
        print(f"Task with id {task_id} not found.")
        return
    with open('db.json', 'w') as file:
        json.dump(tasks, file, indent=4)
    print(f"Task {task_id} updated.")



