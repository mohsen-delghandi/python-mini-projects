from storage import load_contacts, save_contacts

contacts = load_contacts()

def get_contact_id():
    try:
        contact_id = int(input("Enter contact id:"))
        return contact_id
    except ValueError:
        print("Enter a valid Number.")
        return
    
def get_next_id():
    if not contacts:
        return 1
    return max(contact["id"] for contact in contacts) + 1

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
    found = False
    for contact in contacts:
        if contact["id"] == contact_id:
            found = True
            print("What do you want to edit?")
            print("1. Name")
            print("2. Family")
            print("3. Phone")
            print("4. Email")
            print("5. Address")
            print("6. Instagram")
            item_number = int(input("Enter number: "))
            if item_number == 1:
                new_name = input("Enter new name: ")
                contact["name"] = new_name
            elif item_number == 2:
                new_family = input("Enter new family: ")
                contact["family"] = new_family
            elif item_number == 3:
                print("Contact phones:")
                phone_number = 1
                for phone in contact["phones"]:
                    print(f"{phone_number}. {phone}")
                    phone_number += 1
                phone_number = int(input("Enter phone number: "))
                new_phone = input("Enter new phone: ")
                contact["phones"][phone_number - 1] = new_phone
            elif item_number == 4:
                print("Contact emails:")
                email_number = 1
                for email in contact["emails"]:
                    print(f"{email_number}. {email}")
                    email_number += 1
                email_number = int(input("Enter email number: "))
                new_email = input("Enter new email: ")
                contact["emails"][email_number - 1] = new_email
            elif item_number == 5:
                new_address = input("Enter new address: ")
                contact["address"] = new_address
            elif item_number == 6:
                new_instagram = input("Enter new instagram: ")
                contact["instagram"] = new_instagram
            save_contacts(contacts)    
            break
    if not found:
        print("Contact not found.")

def delete_contact():
    contact_id = get_contact_id()
    if contact_id is None:
        return
    found = False
    for contact in contacts:
        if contact["id"] == contact_id:
            found = True
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted.")
            break
    if not found:
        print("Contact not found.")

def toggle_favorite():
    contact_id = get_contact_id()
    if contact_id is None:
        return
    found = False
    for contact in contacts:
        if contact["id"] == contact_id:
            found = True
            contact["favorite"] = not contact["favorite"]
            save_contacts(contacts)
            break
    if not found:
        print("Contact not found.")