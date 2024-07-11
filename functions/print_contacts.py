# Function to print all contacts
def print_contacts(phone_book):
    if not phone_book:
        print("Phone book is empty.")
    else:
        # Iterate through each contact in phone_book and print details
        for idx, contact in enumerate(phone_book, start=1):
            print(
                f"{idx}. {contact['last_name']} {contact['first_name']} {contact['middle_name']}: {contact['phone_number']}"
            )
