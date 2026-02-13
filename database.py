import sqlite3

DB_NAME = "tasks.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            is_completed INTEGER DEFAULT 0
        )
        """)

    conn.commit()
    conn.close()

def add_task_db(name: str, description: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (name, description) VALUES (?, ?)",
        (name, description)
    )

    conn.commit()
    conn.close()

def get_all_tasks():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()

    conn.close()

    tasks = []
    for row in rows:
        tasks.append({
            "id": row[0],
            "name": row[1],
            "description": row[2],
            "is_completed": bool(row[3])
        })

    return tasks

def delete_task_db(task_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))

    conn.commit()
    deleted_count = cursor.rowcount
    conn.close()

    return deleted_count

def update_task_db(task_id: int, new_name: str = None, new_description: str = None, is_completed: bool = None):
    conn = get_connection()
    cursor = conn.cursor()

    fields = []
    values = []

    if new_name is not None:
        fields.append("name = ?")
        values.append(new_name)

    if new_description is not None:
        fields.append("description = ?")
        values.append(new_description)

    if is_completed is not None:
        fields.append("is_completed = ?")
        values.append(int(is_completed))

    if not fields:
        conn.close()
        return 0

    values.append(task_id)

    sql = f"UPDATE tasks SET {', '.join(fields)} WHERE id = ?"
    cursor.execute(sql, values)
    conn.commit()
    updated_count = cursor.rowcount
    conn.close()

    return updated_count