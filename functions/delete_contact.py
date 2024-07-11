# Function to delete a contact
def delete_contact(phone_book, last_name):
    for contact in phone_book:
        if contact['last_name'] == last_name:
            phone_book.remove(contact)
            print(f"Contact {last_name} deleted.")