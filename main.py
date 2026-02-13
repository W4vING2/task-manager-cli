from tasks.filter import *
from tasks.utils import *
from tasks.decors import *

while True:
    print("Welcome to the task manager cli")
    print("1) Add new task")
    print("2) View tasks")
    print("3) Delete task")
    print("4) Update task")
    print("0) Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Add task")
        title = input("Enter new task's title: ")
        description = input("Enter new task's description: ")
        add_task(title, description)
    elif choice == 2:
        print("All tasks")
        print(load_tasks())
        print("1) All tasks")
        print("2) Completed tasks")
        print("3) Incomplete tasks")
        task_choice = int(input("Enter your choice: "))
        if task_choice == 1:
            tasks = sorted(load_tasks(), key=lambda x: x['id'])
        elif task_choice == 2:
            tasks = sorted(filter_tasks(True), key=lambda x: x['id'])
        elif task_choice == 3:
            tasks = sorted(filter_tasks(False), key=lambda x: x['id'])
        for task in tasks:
            print(task)
    elif choice == 3:
        print("Delete task")
        task_id = int(input("Enter task's id: "))
        delete_task(task_id)
    elif choice == 4:
        print("Update task")
        task_id = int(input("Enter task's id: "))
        new_name = input("Enter new task's name: ")
        new_description = input("Enter new task's description: ")
        is_completed = input("Do you have completed the task? (y/n): ")
        update_task(task_id, new_name, new_description, is_completed)
    elif choice == 0:
        break
    else:
        print("Invalid choice")