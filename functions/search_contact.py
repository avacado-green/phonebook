# Function to search for a contact by criteria
def search_contact(phone_book, criteria):
    found = False
    # Iterate through each contact in phone_book
    for contact in phone_book:
        # Check if criteria matches last_name or first_name (case-insensitive)
        if criteria.lower() in contact['last_name'].lower() or \
                criteria.lower() in contact['first_name'].lower():
            print(f"{contact['last_name']} {contact['first_name']} {contact['middle_name']}: {contact['phone_number']}")
            found = True
    if not found:
        print(f"Contact with criteria '{criteria}' not found.")