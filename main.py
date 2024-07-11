from functions.add_contact import add_contact
from functions.edit_contact import edit_contact
from functions.delete_contact import delete_contact
from functions.load_contacts import load_contacts
from functions.save_contacts import save_contacts
from functions.search_contact import search_contact
from functions.print_contacts import print_contacts


# Main function to manage user interaction
def main():
    phone_book = []
    while True:
        print("\n=== PhoneBook ===")
        print("1. Print all contacts")
        print("2. Add a contact")
        print("3. Delete a contact")
        print("4. Edit a contact")
        print("5. Search for a contact")
        print("6. Save to file")
        print("7. Load from file")
        print("0. Exit")

        choice = input("Select an action: ")

        if choice == '1':
            print_contacts(phone_book)
        elif choice == '2':
            last_name = input("Enter last name: ")
            first_name = input("Enter first name: ")
            middle_name = input("Enter middle name: ")
            phone_number = input("Enter phone number: ")
            add_contact(phone_book, last_name, first_name, middle_name, phone_number)
        elif choice == '3':
            last_name = input("Enter last name of contact to delete: ")
            delete_contact(phone_book, last_name)
        elif choice == '4':
            last_name = input("Enter last name of contact to edit: ")
            new_first_name = input("Enter new first name (leave blank to keep current): ")
            new_middle_name = input("Enter new middle name (leave blank to keep current): ")
            new_phone_number = input("Enter new phone number (leave blank to keep current): ")
            edit_contact(phone_book, last_name, new_first_name, new_middle_name, new_phone_number)
        elif choice == '5':
            criteria = input("Enter search criteria (name or last name): ")
            search_contact(phone_book, criteria)
        elif choice == '6':
            filename = input("Enter file name to save: ")
            save_contacts(phone_book, filename)
        elif choice == '7':
            filename = input("Enter file name to load: ")
            phone_book = load_contacts(filename)
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
