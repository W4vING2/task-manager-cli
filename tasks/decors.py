def validate_id(func):
    def wrapper(task_id, *args, **kwargs):
        if not isinstance(task_id, int) or task_id <= 0:
            print("Invalid id")
        return func(task_id, *args, **kwargs)
    return wrapper


def log(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} is running.")
        function =  func(*args, **kwargs)
        print(f"{func.__name__} is finished.")
        return function
    return wrapper