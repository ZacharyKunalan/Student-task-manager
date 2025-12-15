from src.database import initialise_database, insert_task
from src.models import Task

def main():
    # This is safe to run every time
    initialise_database()
    print("Database initialised successfully.")

if __name__ == "__main__":
    main()
