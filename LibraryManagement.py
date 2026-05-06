#Libarary Management System

# ------------------ Book Class ------------------
class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.is_available = True


# ------------------ User Base Class ------------------
class User:
    def __init__(self, name):
        self.name = name
        self.borrowed = []

    def borrow_book(self, book):
        pass

    def return_book(self, book):
        pass


# ------------------ Student Class ------------------
class Student(User):
    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed.append(book)
            print("Book issued to student")
        else:
            print("Book not available")

    def return_book(self, book):
        if book in self.borrowed:
            book.is_available = True
            self.borrowed.remove(book)
            print("Returned by student")
        else:
            print("Not borrowed")


# ------------------ Faculty Class ------------------
class Faculty(User):
    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed.append(book)
            print("Book issued to faculty")
        else:
            print("Book not available")

    def return_book(self, book):
        if book in self.borrowed:
            book.is_available = True
            self.borrowed.remove(book)
            print("Returned by faculty")
        else:
            print("Not borrowed")


# ------------------ Library Class ------------------
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            status = "Available" if book.is_available else "Issued"
            print(book.book_id, book.title, "-", status)

    def search_book(self, name):
        for book in self.books:
            if name.lower() in book.title.lower():
                print("Found:", book.title)


# ------------------ Demo ------------------
lib = Library()

b1 = Book(1, "Python Basics")
b2 = Book(2, "OOP Concepts")

lib.add_book(b1)
lib.add_book(b2)

s1 = Student("Rahul")
f1 = Faculty("Dr. Sharma")

lib.show_books()

s1.borrow_book(b1)
lib.show_books()

s1.return_book(b1)
lib.show_books()