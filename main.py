from src.database import initialise_database, insert_task, get_all_tasks
from src.models import Task

def main():
    initialise_database()
    print("Database initialised successfully.")

    while True:
        print("\n--- Student Task Manager ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            tasks = get_all_tasks()
            if not tasks:
                print("No tasks found.")
            else:
                for t in tasks:
                    print(t)

        elif choice == "2":
            title = input("Title: ").strip()
            deadline = input("Deadline (YYYY-MM-DD): ").strip()
            priority = int(input("Priority (1=High, 2=Medium, 3=Low): ").strip())

            new_task = Task(title=title, deadline=deadline, priority=priority)
            insert_task(new_task)
            print("Task added!")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
