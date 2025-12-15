from src.database import initialise_database, insert_task
from src.models import Task

def main():
    # This is safe to run every time
    initialise_database()
    print("Database initialised successfully.")

    # Temporary test task (we'll remove this later)
    task = Task(
        title="Test task",
        deadline="2025-01-20",
        priority=1
    )

    insert_task(task)
    print("Test task added to database.")

if __name__ == "__main__":
    main()
