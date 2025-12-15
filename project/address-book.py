print("Welcome  to the Address Book Application!")

# uc1
class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.email = email
        
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return (
            f"Name: {self.full_name()}\n"
            f"Address: {self.address}, {self.city}, {self.state}, {self.zip_code}\n"
            f"Phone: {self.phone}\n"
            f"Email: {self.email}"
        )

# uc2       
class AdressBook:
    def __init__(self, name):
        self.name = name
        self.contacts = []
        
    def add_contact(self, contact):
        self.contacts.append(contact)
        
    # uc3
    def edit_contact(self, first_name, last_name):
        for c in self.contacts:
            if c.first_name == first_name and c.last_name == last_name:
                c.address = input("Enter new address: ")
                c.city = input("Enter new city: ")
                c.state = input("Enter new state: ")
                c.zip_code = input("Enter new zip code: ")
                c.phone = input("Enter new phone number: ")
                c.email = input("Enter new email: ")
                print("Contact updated successfully.")
                return
        print("Contact not found.")
        
    # uc4
    def delete_contact(self, first_name, last_name):
        for c in self.contacts:
            if c.first_name == first_name and c.last_name == last_name:
                self.contacts.remove(c)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")
        
    #uc6
    class AddressBookSystem:
        def __init__(self):
            self.address_books = {}
            
        def add_address_book(self, name):
            if name in self.address_books:
                print("Address book with this name already exists.")
                return
            self.address_books[name] = AdressBook(name)
            print(f"Address book '{name}' created successfully.")
        