def add_contact(contacts):
    name = input("Enter contact name: ")
    if name in contacts:
        print("Contact already exists!")
        return

    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    
    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}")

def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ")
    found_contacts = {name: details for name, details in contacts.items() if search_term in name or search_term in details['phone']}
    
    if not found_contacts:
        print("No contact found.")
    else:
        for name, details in found_contacts.items():
            print(f"\nName: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    if name not in contacts:
        print("Contact not found!")
        return

    print("Enter new details (leave blank to keep current value):")
    phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ") or contacts[name]['phone']
    email = input(f"Enter new email (current: {contacts[name]['email']}): ") or contacts[name]['email']
    address = input(f"Enter new address (current: {contacts[name]['address']}): ") or contacts[name]['address']

    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    print("Contact updated successfully!")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def main():
    contacts = {}
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting the contact management system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
