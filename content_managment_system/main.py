import contacts

def display_menu():
    print("\nWelcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file")
    print("8. Quit")

def main():
    while True:
        display_menu()
        choice = input("Select an option (1-8): ")
        try:
            choice = int(choice)
            if choice == 1:
                print("Adding a new contact...")
                contacts.add_contact()
            elif choice == 2:
                print("Editing an existing contact...")
                contacts.edit_contact()
            elif choice == 3:
                print("Deleting a contact...")
                contacts.delete_contact()
            elif choice == 4:
                print("Searching for a contact...")
                contacts.search_contact()
            elif choice == 5:
                print("Displaying all contacts...")
                contacts.display_all_contacts()
            elif choice == 6:
                print("Exporting contacts to a text file...")
                contacts.export_contacts()
            elif choice == 7:
                print("Importing contacts from a text file...")
                contacts.import_contacts()
            elif choice == 8:
                print("Thank you for using the Contact Management System. Goodbye!")
                break
            else:
                print("Please select a valid option (1-8).")
        except ValueError as e:
            print(f"ValueError: {e}")
            print("Please enter a valid number.")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
