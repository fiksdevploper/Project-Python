class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority

    def __str__(self):
        return f"{self.description} (Due: {self.due_date}, Priority: {self.priority})"
