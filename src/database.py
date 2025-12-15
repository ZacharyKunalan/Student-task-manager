import sqlite3

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
