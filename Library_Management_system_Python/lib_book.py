class Book:
    def __init__(self, book_id, title, author,genre):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = True

    def display_details(self):
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre : {self.genre}")
        print(f"Available: {'Yes' if self.available else 'No'}")