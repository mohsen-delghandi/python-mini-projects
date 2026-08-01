from storage import save_tasks, load_tasks
tasks = []

def add_task():
    title = input("Enter task title: ")
    task = {
        "title": title,
        "done": False
    }
    tasks.append(task)
    save_tasks(tasks)

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
        number = int(input("Enter the task number: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    if number < 1 or number > len(tasks):
        print("Invalid task number.")
    else:
        tasks[number - 1]["done"] = True
        save_tasks(tasks)
        print("Task completed.")

def delete_task():
    if not tasks:
        print("No tasks found.")
        return
    try:
        number = int(input("Enter the task number: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    if number < 1 or number > len(tasks):
        print("Invalid task number.")
    else:
        tasks.pop(number - 1)
        save_tasks(tasks)
        print("Task deleted.")

def edit_task():
    if not tasks:
        print("No tasks found.")
        return
    try:
        number = int(input("Enter the task number: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    if number < 1 or number > len(tasks):
        print("Invalid task number.")
        return
    tasks[number - 1]["title"] = input("Enter new title: ")
    save_tasks(tasks)
    print("Task updated.")

tasks = load_tasks()
menu()