class Task:
    def __init__(self, title, deadline, priority, completed=False, task_id=None):
        self.id = task_id
        self.title = title
        self.deadline = deadline
        self.priority = priority
        self.completed = completed

    def __str__(self):
        status = "✔" if self.completed else "✘"
        return f"{self.title} | Due: {self.deadline} | Priority: {self.priority} | {status}"
