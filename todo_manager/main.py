from storage import save_tasks, load_tasks
from datetime import datetime

tasks = []

def add_task():
    title = input("Enter task title: ")
    task = {
        "id": get_next_id(),
        "title": title,
        "done": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    tasks.append(task)
    save_tasks(tasks)

def show_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            if task["done"]:
                print(task["id"], "✅", task["title"])
            else:
                print(task["id"], "⬜", task["title"])
            print("   Created:", task["created_at"])

def menu():
    while True:
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Edit Task")
        print("6. Exit")
        try:      
            selection = int(input("Enter the number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if selection == 1:
            add_task()
        elif selection == 2:
            show_tasks()
        elif selection == 3:
            complete_task()
        elif selection == 4:
            delete_task()
        elif selection == 5:
            edit_task()
        elif selection == 6:
            break
        else:
            print("Invalid option.")
        

def complete_task():
    if not tasks:
        print("No tasks found.")
        return
    try:
        task_id = int(input("Enter task id: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    task = find_task_by_id(task_id)
    
    if task is None:
        print("Task not found.")
        return
    
    task["done"] = True
    save_tasks(tasks)
    print("Task completed.")

def delete_task():
    if not tasks:
        print("No tasks found.")
        return
    try:
        task_id = int(input("Enter task id: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    
    task = find_task_by_id(task_id)

    if task is None:
        print("Task not found.")
        return
    tasks.remove(task)
    save_tasks(tasks)
    print("Task deleted.")

def edit_task():
    if not tasks:
        print("No tasks found.")
        return
    try:
        task_id = int(input("Enter task id: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    task = find_task_by_id(task_id)

    if task is None:
        print("Task not found.")
        return
    
    task["title"] = input("Enter new title: ")
    save_tasks(tasks)
    print("Task updated.")

def get_next_id():
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

def find_task_by_id(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None

tasks = load_tasks()
menu()