class Book:
    def __init__(self, title, author, isbn):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._available = True  # Encapsulated attribute to track availability

    # Getter and Setter for availability
    def is_available(self):
        return self._available

    def set_availability(self, status):
        self._available = status

    def __str__(self):
        return f"Title: {self._title}, Author: {self._author}, ISBN: {self._isbn}, Available: {'Yes' if self._available else 'No'}"


class Member:
    def __init__(self, name, member_id):
        self._name = name
        self._member_id = member_id
        self._borrowed_books = []

    # Getter for borrowed books
    def get_borrowed_books(self):
        return self._borrowed_books

    # Method for borrowing a book (Polymorphic method)
    def borrow_book(self, book):
        if book.is_available():
            book.set_availability(False)
            self._borrowed_books.append(book)
            print(f"{self._name} has borrowed '{book._title}'")
        else:
            print(f"Sorry, '{book._title}' is currently unavailable.")

    # Method for returning a book
    def return_book(self, book):
        if book in self._borrowed_books:
            book.set_availability(True)
            self._borrowed_books.remove(book)
            print(f"{self._name} has returned '{book._title}'")
        else:
            print(f"{self._name} does not have '{book._title}' borrowed.")

    def __str__(self):
        return f"Member: {self._name}, ID: {self._member_id}"


class Librarian(Member):
    # Inherits from Member and has additional privileges for book management

    def __init__(self, name, member_id):
        super().__init__(name, member_id)

    # Method to add a new book to the library collection
    def add_book(self, library, book):
        library.add_book(book)
        print(f"Librarian {self._name} added '{book._title}' to the library.")

    # Method to remove a book from the library collection
    def remove_book(self, library, book):
        if book in library.get_books():
            library.remove_book(book)
            print(f"Librarian {self._name} removed '{book._title}' from the library.")
        else:
            print(f"Book '{book._title}' not found in the library.")

    # Polymorphic method: Librarian borrows differently
    def borrow_book(self, book):
        print("Librarians do not borrow books for personal use.")


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def remove_book(self, book):
        self._books.remove(book)

    # Search feature to find books by title or author
    def search_books(self, query):
        results = [book for book in self._books if query.lower() in book._title.lower() or query.lower() in book._author.lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found matching the search criteria.")

    # Get all books (encapsulated method)
    def get_books(self):
        return self._books

    def display_books(self):
        print("Library Books:")
        for book in self._books:
            print(book)


# Demo of Library Management System
if __name__ == "__main__":
    # Create a library instance
    library = Library()

    # Create some books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")
    book3 = Book("1984", "George Orwell", "1122334455")

    # Create a librarian and a member
    librarian = Librarian("Alice", "L001")
    member = Member("Bob", "M001")

    # Librarian adds books to the library
    librarian.add_book(library, book1)
    librarian.add_book(library, book2)
    librarian.add_book(library, book3)

    # Display all books in the library
    library.display_books()

    # Member borrows a book
    member.borrow_book(book1)
    library.display_books()

    # Member tries to borrow the same book again
    member.borrow_book(book1)

    # Member returns the book
    member.return_book(book1)
    library.display_books()

    # Member searches for a book by title
    library.search_books("1984")

    # Librarian attempts to borrow a book (demonstrates polymorphism)
    librarian.borrow_book(book2)
