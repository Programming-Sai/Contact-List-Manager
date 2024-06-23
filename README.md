
# Contact List Manager

The Contact List Manager is a Python program that allows you to manage your contacts efficiently. You can create, edit, delete, search, and organize your contacts into groups such as friends and family.

## Table of Contents
1. [Features](#features)
2. [Setup](#setup)
3. [Usage](#usage)
4. [Class Documentation](#class-documentation)
5. [Example](#example)
6. [Notes](#notes)

## Features

- **Create Contact:** Add new contacts with name and phone number.
- **Display Contacts:** View all stored contacts.
- **Search Contacts:** Search for contacts by name.
- **Edit Contacts:** Edit contact details (name or phone number).
- **Delete Contacts:** Remove a contact from the list.
- **Organize Contacts:** Add contacts to groups such as friends or family.

## Setup

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/Programming-Sai/Contact-List-Manager.git
   cd Contact-List-Manager
   ```

2. **Install Requirements:**
   No external libraries are required for this program. It runs on standard Python libraries.

## Usage

Run the program using Python:
```sh
python contact_list_manager.py
```

## Class Documentation

### Contact Class

#### Attributes:
- `name`: (str) The name of the contact.
- `num`: (str) The phone number of the contact.
- `contact`: (list) A list of all contacts.
- `friends_contact`: (list) A list of contacts in the friends group.
- `family_contact`: (list) A list of contacts in the family group.

#### Methods:
- `create_contact()`: Prompts the user to enter a name and phone number to create a new contact.
- `display_contact()`: Displays all contacts.
- `search_contact()`: Searches for a contact by name.
- `edit_contact()`: Edits an existing contact's name or phone number.
- `delete_contact()`: Deletes a contact.
- `add_contact()`: Adds a contact to the friends or family group.
- `replace(list_, item, replacement)`: Replaces an item in a list with a new value.

## Example

Here is an example of how to use the Contact List Manager:

1. **Start the Program:**
   ```sh
   python contact_list_manager.py
   ```

2. **Menu Options:**
   - Select an option by entering the corresponding number.
   - Options:
     1. Search for a contact
     2. Display all contacts
     3. Create a new contact
     4. Edit a contact
     5. Delete a contact
     6. Add contact to another group
     7. Exit

3. **Create a New Contact:**
   - Select option `3`.
   - Enter the name and phone number when prompted.

4. **Display Contacts:**
   - Select option `2` to display all stored contacts.

5. **Search for a Contact:**
   - Select option `1` and enter the name of the contact.

6. **Edit a Contact:**
   - Select option `4` and follow the prompts to edit a contact.

7. **Delete a Contact:**
   - Select option `5` to delete a contact.

8. **Add Contact to Group:**
   - Select option `6` to add a contact to the friends or family group.

## Notes

- The phone number must be exactly 10 digits.
- The program prompts the user for confirmation before each major action.
- Use the `menu()` function frequently to keep track of your current location and available actions.

Enjoy managing your contacts with the Contact List Manager!
