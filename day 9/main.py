from task import Task
from data_manager import save_tasks, load_tasks

FILENAME = 'tasks.json'

def add_task(tasks):
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (low, medium, high): ")
    tasks.append(Task(description, due_date, priority))

def delete_task(tasks):
    task_index = int(input("Enter task index to delete: "))
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
    else:
        print("Invalid index")

def list_tasks(tasks):
    for index, task in enumerate(tasks):
        print(f"{index}. {task}")

def main():
    tasks = load_tasks(FILENAME)
    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. Delete task")
        print("3. List tasks")
        print("4. Save and exit")
        choice = input("Enter choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            delete_task(tasks)
        elif choice == '3':
            list_tasks(tasks)
        elif choice == '4':
            save_tasks(tasks, FILENAME)
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
