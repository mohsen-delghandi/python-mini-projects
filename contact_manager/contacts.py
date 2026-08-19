from storage import load_contacts, save_contacts
from utils import get_number

contacts = load_contacts()

def get_contact_id():
    return get_number("Enter contact id:")
     
    
def get_next_id():
    if not contacts:
        return 1
    return max(contact["id"] for contact in contacts) + 1

def find_contact(contact_id):
    for contact in contacts:
        if contact_id == contact["id"]:
            return contact

def add_contact():
    name = input("Name: ")
    family = input("Family: ")
    phone = input("Phone: ")
    email = input("Email: ")

    contact = {
        "id": get_next_id(),
        "name": name,
        "family": family,
        "phones": [
            phone
        ],
        "emails": [
            email
        ],
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
    print("Phone: " + contact["phones"][0])
    print("Email: " + contact["emails"][0])
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
    contact = find_contact(contact_id)
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
            new_name = input("Enter new name: ")
            contact["name"] = new_name
        elif item_number == 2:
            new_family = input("Enter new family: ")
            contact["family"] = new_family
        elif item_number == 3:
            edit_list(contact["phones"], "Enter new phone: ")
        elif item_number == 4:
            edit_list(contact["emails"], "Enter new email: ")
        elif item_number == 5:
            new_address = input("Enter new address: ")
            contact["address"] = new_address
        elif item_number == 6:
            new_instagram = input("Enter new instagram: ")
            contact["instagram"] = new_instagram
        save_contacts(contacts)   
    else:
        print("Contact not found.")

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
    

def delete_contact():
    contact_id = get_contact_id()
    if contact_id is None:
        return
    contact = find_contact(contact_id)
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
    contact = find_contact(contact_id)
    if contact is not None:
        contact["favorite"] = not contact["favorite"]
        save_contacts(contacts)
    else:
        print("Contact not found.")