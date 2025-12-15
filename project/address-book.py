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
    
    # uc2 + uc7 (duplicate check)
    def add_contact(self, contact):
        for c in self.contacts:
            if c.full_name() == contact.full_name():
                print("Contact with this name already exists.")
                return
        self.contacts.append(contact)
        print("Contact added successfully.")
        
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
        
    # UC11
    def sort_by_name(self):
        self.contacts.sort(key=lambda c: (c.first_name, c.last_name))
        print("Contacts sorted by name.")
        
    # UC12
    def sort_by_city(self):
        self.contacts.sort(key=lambda c: c.city)
        print("Contacts sorted by city.")
    
    # UC12
    def sort_by_state(self):
        self.contacts.sort(key=lambda c: c.state)
        print("Contacts sorted by state.")
        
    # UC12
    def sort_by_zip(self):
        self.contacts.sort(key=lambda c: c.zip_code)
        print("Contacts sorted by zip code.")
    
        
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
            
        #uc8
        def search_Person_by_City_or_State(self, city, state):
            results = []
            for book in self.address_books.values():
                for c in book.contacts:
                    if c.city == city or c.state == state:
                        results.append(c)
            return results
        
        # uc9
        def view_by_City(self):
            city_map = {}
            for book in self.address_books.values():
                for c in book.contacts:
                    city_map.setdefault(c.city, []).append(c)
            
            for city, people in city_map.items():
                print(f"City: {city}")
                for p in people:
                    print(p)
          
        # uc9          
        def view_by_State(self):
            state_map = {}
            for book in self.address_books.values():
                for c in book.contacts:
                    state_map.setdefault(c.state, []).append(c)
            
            for state, people in state_map.items():
                print(f"State: {state}")
                for p in people:
                    print(p)
                    
        # uc10
        def count_by_City(self):
            city_count = {}
            for book in self.address_books.values():
                for c in book.contacts:
                    city_count[c.city] = city_count.get(c.city, 0) + 1
            print(city_count)
            
        # uc10
        def count_by_State(self):
            state_count = {}
            for book in self.address_books.values():
                for c in book.contacts:
                    state_count[c.state] = state_count.get(c.state, 0) + 1
            print(state_count)