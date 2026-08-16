from contacts import (
    add_contact,
    show_contacts,
    search_contact,
    edit_contact,
    delete_contact,
    toggle_favorite
)

def main():
    while True:
        print("1. Add Contact")
        print("2. Show Contacts")
        print("3. Search Contact")
        print("4. Edit Contacts")
        print("5. Delete Contact")
        print("6. Toggle Favorite")
        print("7. Exit")
        print("---")
        item_number = get_menu_choice()
        if item_number is None:
            continue
        if item_number == 7 :
            break
        elif item_number == 1 :
            add_contact()
        elif item_number == 2 :
            show_contacts()
        elif item_number == 3 :
            search_contact()
        elif item_number == 4 :
            edit_contact()
        elif item_number == 5 :
            delete_contact()
        elif item_number == 6 :
            toggle_favorite()

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

if __name__ == "__main__":
    main()
    