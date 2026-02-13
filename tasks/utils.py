from database import *
from tasks.decors import *

@log
def add_task(name: str, description: str) -> None:
    add_task_db(name, description)
    print("Task added.")

@log
@validate_id
def delete_task(task_id: int) -> None:
    deleted = delete_task_db(task_id)

    if deleted == 0:
        print("Task not found.")
    else:
        print(f"Task {task_id} deleted.")

@log
@validate_id
def update_task(task_id: int, new_name: str = None, new_description: str = None, is_completed: str = None):
    completed = None
    if is_completed == 'y':
        completed = True
    elif is_completed == 'n':
        completed = False

    updated = update_task_db(task_id, new_name, new_description, completed)

    if updated == 0:
        print(f"Task with id {task_id} not found or nothing to update.")
    else:
        print(f"Task {task_id} updated.")


