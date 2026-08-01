import json

tasks = []

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def load_tasks():
    global tasks
    with open("tasks.json", "r") as file:
        tasks = json.load(file)

def add_task():
    title = input("Enter task title: ")
    task = {
        "title": title,
        "done": False
    }
    tasks.append(task)
    save_tasks()

def show_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks, start=1):
            # status = "✅" if task["done"] else "⬜"
            # print(index, status, task["title"])
            if task["done"]:
                print(index, "✅", task["title"])
            else:
                print(index, "⬜", task["title"])

def menu():
    while True:
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        selection = int(input("Enter the number: "))
        if selection == 1:
            add_task()
        elif selection == 2:
            show_tasks()
        elif selection == 3:
            complete_task()
        elif selection == 4:
            delete_task()
        elif selection == 5:
            break
        else:
            print("Invalid option.")

def complete_task():
    if not tasks:
        print("No tasks found.")
        return
    number = int(input("Enter the task number: "))
    if number < 1 or number > len(tasks):
        print("Invalid task number.")
    else:
        tasks[number - 1]["done"] = True
        save_tasks()
        print("Task completed.")

def delete_task():
    if not tasks:
        print("No tasks found.")
        return
    number = int(input("Enter the number: "))
    if number < 1 or number > len(tasks):
        print("Invalid task number.")
    else:
        tasks.pop(number - 1)
        save_tasks()
        print("Task deleted.")

load_tasks()
menu()