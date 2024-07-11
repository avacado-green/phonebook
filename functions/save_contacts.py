# Function to save contacts to a file
def save_contacts(phone_book, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        # Write each contact's details to the file
        for contact in phone_book:
            file.write(
                f"{contact['last_name']},{contact['first_name']},{contact['middle_name']},{contact['phone_number']}\n")
    print(f"Data saved to file {filename}")