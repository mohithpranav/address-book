print("Welcome  to the Address Book Application!")

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
        
        
class AdressBook:
    def __init__(self, name):
        self.name = name
        self.contacts = []
        
    def add_contact(self, contact):
        self.contacts.append(contact)