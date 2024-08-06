# Develop a program that allows users to store and manage contact information. The program should provide options to
# add a new contact by entering their name, phone number, and email address. It should also allow users to view their
# contact list, edit existing contacts, and delete contacts if needed. The program should store the contacts in
# memory or in a file for persistent storage.


import json
import os

# File where contacts are stored
CONTACTS_FILE = 'contacts.json'


def load_contacts():
    """Load contacts from the file."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return {}


def save_contacts(contacts):
    """Save contacts to the file."""
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter the contact's name: ").strip()
    phone = input("Enter the contact's phone number: ").strip()
    email = input("Enter the contact's email address: ").strip()

    if name in contacts:
        print("Contact with this name already exists.")
    else:
        contacts[name] = {'phone': phone, 'email': email}
        print("Contact added successfully.")


def view_contacts(contacts):
    """View all contacts."""
    if not contacts:
        print("No contacts to display.")
    else:
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")


def edit_contact(contacts):
    """Edit an existing contact."""
    name = input("Enter the name of the contact to edit: ").strip()
    if name in contacts:
        phone = input("Enter the new phone number: ").strip()
        email = input("Enter the new email address: ").strip()
        contacts[name] = {'phone': phone, 'email': email}
        print("Contact updated successfully.")
    else:
        print("Contact not found.")


def delete_contact(contacts):
    """Delete a contact."""
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def main():
    contacts = load_contacts()

    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("Contacts saved. Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
