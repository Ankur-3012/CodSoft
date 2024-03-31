class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")

    def search_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")

    def update_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                contact.name = input("Enter new name: ")
                contact.phone_number = input("Enter new phone number: ")
                contact.email = input("Enter new email: ")
                contact.address = input("Enter new address: ")
                print("Contact updated successfully!")

    def delete_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                self.contacts.remove(contact)
                print("Contact deleted successfully!")

contact_book = ContactBook()
contact1 = Contact("John Doe", "1234567890", "john@example.com", "123 Main St")
contact_book.add_contact(contact1)
contact2 = Contact("Jane Smith", "9876543210", "jane@example.com", "456 Elm St")
contact_book.add_contact(contact2)
contact_book.view_contacts()
contact_book.search_contact("John")
contact_book.update_contact("John Doe")
contact_book.delete_contact("Jane Smith")