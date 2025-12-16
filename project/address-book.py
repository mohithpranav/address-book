import csv
import json

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
    
    # UC13
    def write_to_file(self, filename):
        with open(filename, 'w') as file:
            for c in self.contacts:
                file.write(str(c) + "\n\n")
        print("Data written to file successfully.")
    
    def read_from_file(self, filename):
        with open(filename, 'r') as file:
            print ("\n" + file.read())
            
    # uc14
    def write_csv(self, filename):
        with open(filename, 'w', newline= '') as f:
            writer = csv.writer(f)
            for c in self.contacts:
                writer.writerow([c.first_name, c.last_name, c.address, c.city, c.state, c.zip_code, c.phone, c.email])
        print("Data written to CSV file successfully.")
        
    def read_csv(self, filename):
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            self.contacts.clear()
            for row in reader:
                self.contacts.append(Contact(*row))
        print("Data read from CSV file successfully.")
        
    # uc15
    def write_to_json(self, filename):
        with open(filename, 'w') as f:
            json.dump([c.__dict__ for c in self.contacts], f, indent=4)
        print("Data written to JSON file successfully.")
        
    # uc15
    def read_from_json(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            self.contacts.clear()
            for c in data:
                self.contacts.append(Contact(**c))
        print("Data read from JSON file successfully.")
        
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
            
                  
# ================== MAIN PROGRAM ==================
def main():
    print("Welcome to Address Book Program (UC1–UC14)")
    system = AddressBookSystem()
    system.add_address_book("Default")
    book = system.address_books["Default"]

    while True:
        print("\n1. Add Contact")
        print("2. Edit Contact")
        print("3. Delete Contact")
        print("4. Display Contacts")
        print("5. Sort by Name")
        print("6. Sort by City")
        print("7. Sort by State")
        print("8. Sort by Zip")
        print("9. Write to File")
        print("10. Read from File")
        print("11. Write CSV")
        print("12. Read CSV")
        print("13. Search by City")
        print("14. Search by State")
        print("15. Count by City")
        print("16. Count by State")
        print("17. Write to JSON")
        print("18. Read from JSON")
        print("19. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            contact = Contact(
                input("First Name: "),
                input("Last Name: "),
                input("Address: "),
                input("City: "),
                input("State: "),
                input("Zip: "),
                input("Phone: "),
                input("Email: ")
            )
            book.add_contact(contact)

        elif choice == "2":
            book.edit_contact(input("First Name: "), input("Last Name: "))

        elif choice == "3":
            book.delete_contact(input("First Name: "), input("Last Name: "))

        elif choice == "4":
            for c in book.contacts:
                print(c)

        elif choice == "5":
            book.sort_by_name()
            print("Sorted by name")

        elif choice == "6":
            book.sort_by_city()
            print("Sorted by city")
            
        elif choice == "7":
            book.sort_by_state()
            print("Sorted by state")

        elif choice == "8":
            book.sort_by_zip()
            print("Sorted by zip")

        elif choice == "9":
            book.write_to_file("addressbook.txt")

        elif choice == "10":
            book.read_from_file("addressbook.txt")

        elif choice == "11":
            book.write_csv("addressbook.csv")

        elif choice == "12":
            book.read_csv("addressbook.csv")

        elif choice == "13":
            system.search_by_city_or_state(city=input("Enter City: "))

        elif choice == "14":
            system.search_by_city_or_state(state=input("Enter State: "))

        elif choice == "15":
            system.count_by_city()

        elif choice == "16":
            system.count_by_state()

        elif choice == "17":
            book.write_to_json("addressbook.json")

        elif choice == "18":
            book.read_from_json("addressbook.json")

        elif choice == "19":
            print("Exiting Program")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()