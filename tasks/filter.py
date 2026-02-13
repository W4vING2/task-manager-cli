from tasks.utils import *

def filter_tasks(completed=None):
    tasks = load_tasks()
    if completed is True:
        tasks = [t for t in tasks if t['is_completed']]
    elif completed is False:
        tasks = [t for t in tasks if not t['is_completed']]
    return tasks