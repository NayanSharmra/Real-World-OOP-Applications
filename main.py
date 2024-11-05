class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def lend(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_book(self):
        self.is_available = True

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.lend():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} doesn't have '{book.title}'.")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' to the library.")

    def display_books(self):
        for book in self.books:
            status = "Available" if book.is_available else "Not Available"
            print(f"{book} - {status}")

# Main program with user input
library = Library()
members = {}

while True:
    print("\nLibrary Management System")
    print("1. Add a Book")
    print("2. Display All Books")
    print("3. Register a Member")
    print("4. Borrow a Book")
    print("5. Return a Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        isbn = input("Enter book ISBN: ")
        book = Book(title, author, isbn)
        library.add_book(book)

    elif choice == "2":
        print("\nList of Books in the Library:")
        library.display_books()

    elif choice == "3":
        name = input("Enter member's name: ")
        member_id = input("Enter member ID: ")
        members[member_id] = Member(name, member_id)
        print(f"Registered member '{name}' with ID '{member_id}'.")

    elif choice == "4":
        member_id = input("Enter member ID: ")
        if member_id not in members:
            print("Member not found. Please register first.")
            continue

        title = input("Enter title of the book to borrow: ")
        book_to_borrow = next((b for b in library.books if b.title == title), None)
        
        if book_to_borrow:
            members[member_id].borrow_book(book_to_borrow)
        else:
            print("Book not found in the library.")

    elif choice == "5":
        member_id = input("Enter member ID: ")
        if member_id not in members:
            print("Member not found. Please register first.")
            continue

        title = input("Enter title of the book to return: ")
        book_to_return = next((b for b in library.books if b.title == title), None)
        
        if book_to_return:
            members[member_id].return_book(book_to_return)
        else:
            print("Book not found in the library.")

    elif choice == "6":
        print("Exiting Library Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
