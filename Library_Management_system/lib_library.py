from lib_book import Book
from lib_user import User
class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def display_all_books(self):
        print("All Books in Library:")
        for book in self.books:
            book.display_details()
            print("---------")

    def display_all_users(self):
        print("All Users in Library:")
        for user in self.users:
            user.display_details()
            print("---------")

    def borrow_book(self, user, book):
        if book.available:
            book.available = False
            user.borrowed_books.append(book)
            print(f"{user.name} has successfully borrowed {book.title}")
        else:
            print(f"{book.title} is not available")

    def return_book(self, user, book):
        if book in user.borrowed_books:
            book.available = True
            user.borrowed_books.remove(book)
            print(f"{user.name} has successfully returned {book.title}")
        else:
            print(f"{user.name} has not borrowed {book.title}")
    
