from lib_book import Book
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

    def display_details(self):
        print(f"User ID: {self.user_id}")
        print(f"Name: {self.name}")
        print("Borrowed Books: ")
        if self.borrowed_books:
            for book in self.borrowed_books:
                print(f" Title: {book.title} (Book ID: {book.book_id})")
        else:
            print("No Books Borrowed")