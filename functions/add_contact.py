# Function to add a contact
def add_contact(phone_book, last_name, first_name, middle_name, phone_number):
    # Create a new contact dictionary and append to phone_book
    contact = {
        'last_name': last_name,
        'first_name': first_name,
        'middle_name': middle_name,
        'phone_number': phone_number
    }
    phone_book.append(contact)
