import os

TODO_FILE = "Todo.txt"

def load_tasks():
    """
    Load tasks from the text file.5
    """
    tasks = []
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    """
    Save tasks to the text file.
    """
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def display_tasks(tasks):
    """
    Display the list of tasks.
    """
    print("Todo List:")
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks.")

def add_task(task, tasks):
    """
    Add a task to the list.
    """
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added successfully.")

def mark_completed(index, tasks):
    """
    Mark a task as completed.
    """
    if 1 <= index <= len(tasks):
        completed_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Task '{completed_task}' marked as completed.")
    else:
        print("Invalid task index.")

def delete_task(index, tasks):
    """
    Delete a task from the list.
    """
    if 1 <= index <= len(tasks):
        deleted_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Task '{deleted_task}' deleted successfully.")
    else:
        print("Invalid task index.")

def main():
    tasks = load_tasks()

    while True:
        print("\nOptions:")
        print("1. Display Todo List")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            task = input("Enter the task: ")
            add_task(task, tasks)
        elif choice == "3":
            index = int(input("Enter the index of the task to mark as completed: "))
            mark_completed(index, tasks)
        elif choice == "4":
            index = int(input("Enter the index of the task to delete: "))
            delete_task(index, tasks)
        elif choice == "5":
            print("Exiting the Todo List application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
