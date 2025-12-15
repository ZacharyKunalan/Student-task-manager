import sqlite3
from src.models import Task


DB_NAME = "tasks.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def initialise_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            deadline TEXT NOT NULL,
            priority INTEGER NOT NULL,
            completed INTEGER DEFAULT 0
        );
    """)

    conn.commit()
    conn.close()

def insert_task(task):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tasks (title, deadline, priority, completed)
        VALUES (?, ?, ?, ?)
    """, (
        task.title,
        task.deadline,
        task.priority,
        int(task.completed)
    ))

    conn.commit()
    conn.close()

def get_all_tasks():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, title, deadline, priority, completed FROM tasks")
    rows = cursor.fetchall()

    conn.close()

    tasks = []
    for row in rows:
        task_id, title, deadline, priority, completed = row
        tasks.append(Task(title, deadline, priority, bool(completed), task_id))

    return tasks

