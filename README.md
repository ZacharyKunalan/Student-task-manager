# Student Task Manager

## 📌 Project Overview

The **Student Task Manager** is a command-line application built in Python that helps students manage their tasks efficiently. Users can add tasks, view all tasks, mark tasks as completed, and delete tasks. All task data is stored persistently using an SQLite database.

This project demonstrates core programming concepts such as database management, modular design, and basic CRUD (Create, Read, Update, Delete) operations.

---

## 🎯 Features

* Add new tasks with a title, deadline, and priority
* View all existing tasks in a clean, readable format
* Mark tasks as completed
* Delete tasks by ID
* Persistent storage using SQLite

---

## 🛠️ Technologies & Tools Used

* **Python 3** – Main programming language
* **SQLite** – Lightweight relational database for persistent data storage
* **sqlite3 (Python standard library)** – Database connectivity
* **VS Code** – Code editor
* **SQLite Explorer (VS Code Extension)** – Database inspection and debugging

---

## 🗂️ Project Structure

```
project-root/
│
├── main.py              # Entry point and CLI loop
├── tasks.db             # SQLite database file
└── src/
    ├── database.py      # Database logic (SQL operations)
    └── models.py        # Task model
```

---

## 🧠 Design Overview

The application follows a **layered architecture**:

* **models.py** defines the `Task` data model
* **database.py** handles all SQL and database interactions
* **main.py** manages user input and application flow

This separation of concerns improves readability, maintainability, and scalability.

---

## ▶️ How to Run the Project

1. Ensure Python 3 is installed
2. Clone or download the project files
3. Run the application:

```bash
python main.py
```

4. Follow the on-screen menu to manage tasks

The database will be automatically created and initialized on first run.

---

## 📚 Learning Outcomes

* Working with SQLite databases in Python
* Writing safe SQL queries using placeholders
* Structuring a Python project professionally
* Implementing CRUD functionality
* Understanding the `__main__` entry point pattern

---

## ✍️ Author

This project was created as a **student task management application** for learning and academic purposes.

---

## ✅ Future Improvements (Optional)

* Input validation for dates and priorities
* Sorting tasks by deadline or priority
* Search functionality
* GUI version using Tkinter or PyQt

---

Thank you for reviewing this project!
