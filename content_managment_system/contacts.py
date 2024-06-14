# contacts.py

contacts = {}

def add_contact():
    identifier = input("Enter a unique identifier (e.g., email or phone number): ")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    additional_info = input("Enter additional information (optional): ")
    contacts[identifier] = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Additional Info": additional_info
    }
    print("Contact added successfully!")

def edit_contact():
    identifier = input("Enter the unique identifier of the contact to edit: ")
    if identifier in contacts:
        print(f"Editing contact: {contacts[identifier]}")
        name = input("Enter new name (leave blank to keep current): ")
        phone = input("Enter new phone number (leave blank to keep current): ")
        email = input("Enter new email address (leave blank to keep current): ")
        additional_info = input("Enter new additional information (leave blank to keep current): ")
        
        if name:
            contacts[identifier]["Name"] = name
        if phone:
            contacts[identifier]["Phone"] = phone
        if email:
            contacts[identifier]["Email"] = email
        if additional_info:
            contacts[identifier]["Additional Info"] = additional_info
        
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

def delete_contact():
    identifier = input("Enter the unique identifier of the contact to delete: ")
    if identifier in contacts:
        del contacts[identifier]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def search_contact():
    identifier = input("Enter the unique identifier of the contact to search for: ")
    if identifier in contacts:
        print(f"Contact details: {contacts[identifier]}")
    else:
        print("Contact not found!")

def display_all_contacts():
    if contacts:
        print("All contacts:")
        for identifier, details in contacts.items():
            print(f"Identifier: {identifier}")
            for key, value in details.items():
                print(f"  {key}: {value}")
    else:
        print("No contacts found.")

def export_contacts():
    filename = input("Enter the filename to export contacts to: ")
    try:
        with open(filename, 'w') as f:
            for identifier, details in contacts.items():
                f.write(f"Identifier: {identifier}\n")
                for key, value in details.items():
                    f.write(f"  {key}: {value}\n")
                f.write("\n")
        print("Contacts exported successfully!")
    except Exception as e:
        print(f"An error occurred while exporting contacts: {e}")

def import_contacts():
    filename = input("Enter the filename to import contacts from: ")
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            new_contact = {}
            for line in lines:
                if line.strip() == "":
                    if new_contact:
                        contacts[new_contact["Identifier"]] = new_contact
                        new_contact = {}
                else:
                    key, value = line.strip().split(": ", 1)
                    if key == "Identifier":
                        new_contact["Identifier"] = value
                    else:
                        new_contact[key] = value
            if new_contact:
                contacts[new_contact["Identifier"]] = new_contact
        print("Contacts imported successfully!")
    except Exception as e:
        print(f"An error occurred while importing contacts: {e}")
