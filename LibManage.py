class Book:
    def __init__(self, name):
        self.name = name
        self.available = True


class Patron:
    def __init__(self, name):
        self.name = name


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, name):
        self.books.append(Book(name))
        print("Book added")

    def add_patron(self, name):
        self.patrons.append(Patron(name))
        print("Patron added")

    def borrow_book(self, name):
        for book in self.books:
            if book.name == name and book.available:
                book.available = False
                print("Book borrowed")
                return
        print("Book not available")

    def return_book(self, name):
        for book in self.books:
            if book.name == name:
                book.available = True
                print("Book returned")
                return
        print("Book not found")

    def show_books(self):
        for book in self.books:
            if book.available:
                print(book.name, "- Available")
            else:
                print(book.name, "- Borrowed")


library = Library()

n = int(input("How many books do you want to add? "))

for i in range(n):
    library.add_book(input("Enter book name: "))

m = int(input("How many patrons do you want to add? "))

for i in range(m):
    library.add_patron(input("Enter patron name: "))

library.show_books()

book = input("Enter book to borrow: ")
library.borrow_book(book)

library.show_books()

book = input("Enter book to return: ")
library.return_book(book)

library.show_books()