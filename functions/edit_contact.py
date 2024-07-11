# Function to edit a contact
def edit_contact(phone_book, last_name, new_first_name=None, new_middle_name=None, new_phone_number=None):
    for contact in phone_book:
        if contact['last_name'] == last_name:
            # Update contact details if new values are provided
            if new_first_name:
                contact['first_name'] = new_first_name
            if new_middle_name:
                contact['middle_name'] = new_middle_name
            if new_phone_number:
                contact['phone_number'] = new_phone_number
            print(f"Contact {last_name} updated.")
