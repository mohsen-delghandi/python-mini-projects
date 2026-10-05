from storage import load_contacts, save_contacts
from utils import get_number

contacts = load_contacts()

def get_contact_id():
    return get_number("Enter contact id:")
     
    
def get_next_id():
    if not contacts:
        return 1
    return max(contact["id"] for contact in contacts) + 1

def find_contact(contact_id, contacts):
    for contact in contacts:
        if contact_id == contact["id"]:
            return contact

def get_list_items(prompt):
    items = []

    while True:
        item = input(prompt)

        if not item:
            print("Field empty.")
            continue

        items.append(item)

        answer = input("Add another? (y/n): ").lower()

        if answer != "y":
            break

    return items

def add_contact():
    name = input("Name: ")
    family = input("Family: ")

    contact = {
        "id": get_next_id(),
        "name": name,
        "family": family,
        "phones": get_list_items("Phone: "),
        "emails": get_list_items("Email: "),
        "address": "Tehran",
        "image": "",
        "instagram": "@ali",
        "favorite": False
    }
    contacts.append(contact)
    save_contacts(contacts)

def display_contact(contact):
    print("----------------------")
    print("ID: " ,contact["id"])
    print(f"Name: {contact['name']}  {contact['family']}")
    print("Phone:")
    if len(contact["phones"]) == 0:
        print("No Phone numbers.")
    else:
        for number, item in enumerate(contact["phones"], start=1):
            print(f"{number}. {item}")
    print("Emails:")
    if len(contact["emails"]) == 0:
        print("No emails.")
    else:
        for number, item in enumerate(contact["emails"], start=1):
            print(f"{number}. {item}")    
    if contact["favorite"]:
        print("Favorite: Yes")
    else:
        print("Favorite: No")
    print("----------------------")

def show_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for contact in contacts:
            display_contact(contact)

def search_contact():
    search_string = input("Enter the name: ")
    found = False
    for contact in contacts:
        if contact["name"].lower() == search_string.lower() or contact["family"].lower() == search_string.lower():
            display_contact(contact)
            found = True
    if not found:
        print("Contact not found.")
        
def edit_contact():
    contact_id = get_contact_id()
    if contact_id is None:
        return
    contact = find_contact(contact_id,contacts)
    if contact is not None:
        print("What do you want to edit?")
        print("1. Name")
        print("2. Family")
        print("3. Phone")
        print("4. Email")
        print("5. Address")
        print("6. Instagram")
        item_number = get_number("Enter number: ")
        if item_number is None:
            return
        if not 1 <= item_number <=6:
            print("Wrong choice.")
            return
        if item_number == 1:
            edit_value(contact, "name", "Enter new name: ")
        elif item_number == 2:
            edit_value(contact, "family", "Enter new family: ")            
        elif item_number == 3:
            manage_list(contact["phones"],"Enter new phone: ")
        elif item_number == 4:
            manage_list(contact["emails"],"Enter new email: ")
        elif item_number == 5:
            edit_value(contact, "address", "Enter new address: ")
        elif item_number == 6:            
            edit_value(contact, "instagram", "Enter new instagram: ")

        save_contacts(contacts)   
    else:
        print("Contact not found.")

def delete_list_item(items):
    item_number = get_number("Enter item number: ")
    if item_number is None:
        print("Enter a valid number.")
        return
    if not 1 <= item_number <= len(items):
        print("Item doesnt exist.")
        return
    items.pop(item_number - 1)
    print("Item deleted.")

def add_list_item(items, prompt):
    new_value = input(prompt)
    if new_value == "":
        print("Field empty.")
        return
    items.append(new_value)

def manage_list(items, prompt):
    print("1. Edit")
    print("2. Delete")
    print("3. Add")
    number = get_number("Select an item: ")
    if number is None:
        print("Invalid choice.")
        return
    if number == 1:
        edit_list(items, prompt)
    elif number == 2:
        delete_list_item(items)
    elif number == 3:
        add_list_item(items, prompt)
    else:
        print("Wrong choice.")


def edit_list(items, prompt):
    for number, item in enumerate(items, start=1):
        print(f"{number}: {item}")
    item_number = get_number("Enter the item number: ")
    if item_number is None:
        print("Invalid item number: ")
        return
    if not 1 <= item_number <=len(items):
        print("Invalid item number: ")
        return
    new_value = input(prompt)
    items[item_number - 1] = new_value

def edit_value(contact, field, prompt):
    new_value = input(prompt)
    contact[field] = new_value

def delete_contact():
    contact_id = get_contact_id()
    if contact_id is None:
        return
    contact = find_contact(contact_id, contacts)
    if contact is not None:
        contacts.remove(contact)
        save_contacts(contacts)
        print("Contact deleted.")            
    else:
        print("Contact not found.")

def toggle_favorite():
    contact_id = get_contact_id()
    if contact_id is None:
        return
    contact = find_contact(contact_id,contacts)
    if contact is not None:
        contact["favorite"] = not contact["favorite"]
        save_contacts(contacts)
    else:
        print("Contact not found.")