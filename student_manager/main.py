students = []

def add_student():
    name = input("Enter student name: ")
    students.append(name)
    print("Student added successfully.")

def show_students():
    if not students:
        print("No students found.")
    else:
        for student in students:
            print(student)

def menu():
    while True:
        print("1. Add Student")
        print("2. Show Students")
        print("3. Exit")
        selection = int(input("Please select the item: "))
        if selection == 3:
            print("Goodbye!")
            break
        elif selection == 1:
            add_student()
        elif selection == 2:
            show_students()
        else:
            print("Invalid option.")

menu()