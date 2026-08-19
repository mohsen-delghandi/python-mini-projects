def get_menu_choice():
    try:
        item_number = int(input("Please select item:"))
    except ValueError:
        print("Invalid option.")
        return
    if 1 <= item_number <= 7:
        return item_number
    else:
        print("Invalid option.")

def get_number(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Please enter a valid number.")
        return None