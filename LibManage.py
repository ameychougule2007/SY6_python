class Book:
    def __init__(self, title):
        self.title = title
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True

    def return_book(self):
        self.is_borrowed = False


class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        self.borrowed_books.remove(book)


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)

    def register_patron(self, patron):
        self.patrons.append(patron)

    def borrow_book(self, book, patron):
        if not book.is_borrowed:
            book.borrow()
            patron.borrow_book(book)
            print("Book issued successfully")
        else:
            print("Book is already issued")

    def return_book(self, book, patron):
        if book in patron.borrowed_books:
            book.return_book()
            patron.return_book(book)
            print("Book returned successfully")
        else:
            print("Book was not issued to this patron")


library = Library()

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Add Patron")
    print("4. View Patrons")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        library.add_book(Book(title))
        print("Book added successfully")

    elif choice == "2":
        if len(library.books) == 0:
            print("No books available")
        else:
            print("\nBooks:")
            for i in range(len(library.books)):
                status = "Issued" if library.books[i].is_borrowed else "Available"
                print(i + 1, library.books[i].title, "-", status)

    elif choice == "3":
        name = input("Enter patron name: ")
        patron_id = input("Enter patron ID: ")
        library.register_patron(Patron(name, patron_id))
        print("Patron registered successfully")

    elif choice == "4":
        if len(library.patrons) == 0:
            print("No patrons registered")
        else:
            print("\nPatrons:")
            for i in range(len(library.patrons)):
                print(i + 1, library.patrons[i].name, "-", library.patrons[i].patron_id)

    elif choice == "5":
        if len(library.books) == 0 or len(library.patrons) == 0:
            print("Add books and patrons first")
        else:
            print("\nBooks:")
            for i in range(len(library.books)):
                print(i + 1, library.books[i].title)

            book_number = int(input("Enter book number: ")) - 1

            print("\nPatrons:")
            for i in range(len(library.patrons)):
                print(i + 1, library.patrons[i].name)

            patron_number = int(input("Enter patron number: ")) - 1

            library.borrow_book(
                library.books[book_number],
                library.patrons[patron_number]
            )

    elif choice == "6":
        if len(library.books) == 0 or len(library.patrons) == 0:
            print("Add books and patrons first")
        else:
            print("\nBooks:")
            for i in range(len(library.books)):
                print(i + 1, library.books[i].title)

            book_number = int(input("Enter book number: ")) - 1

            print("\nPatrons:")
            for i in range(len(library.patrons)):
                print(i + 1, library.patrons[i].name)

            patron_number = int(input("Enter patron number: ")) - 1

            library.return_book(
                library.books[book_number],
                library.patrons[patron_number]
            )

    elif choice == "7":
        print("Thank you for using the Library Management System")
        break

    else:
        print("Invalid choice")
