from functions.add_contact import add_contact


# Function to load contacts from a file
def load_contacts(filename):
    inner_phone_book = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            # Read each line from the file, split into fields and add as new contact
            for line in file:
                last_name, first_name, middle_name, phone_number = line.strip().split(',')
                add_contact(inner_phone_book, last_name, first_name, middle_name, phone_number)
        print(f"Data loaded from file {filename}")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    return inner_phone_book
