from lib_book import Book
from lib_user import User
from lib_library import Library

def print_menu():
    print("\n====== Online Library Management System======")
    print("1. Add Book")
    print("2. Add User")
    print("3. Display All Books")
    print("4. Display All Users")
    print("5. Borrow Book")
    print("6. Return Book")
    print("0. Exit")

library = Library()

def get_user_by_id(user_id):
    for user in library.users:
        if user.user_id == user_id:
            return user
    return None

def get_book_by_id(book_id):
    for book in library.books:
        if book.book_id == book_id:
            return book
    return None

def main():
    while True:
        print_menu()
        choice = input("Enter your choice : ")

        if choice == '1':
            book_id = int(input("Enter Book ID : "))
            title = input("Enter Title : ")
            author = input("Enter Author : ")
            genre = input("Enter Genre : ")
            new_book = Book(book_id, title, author, genre)
            library.add_book(new_book)
            print(f"Book '{title}' added to Library")

        elif choice == '2':
            user_id = int(input("Enter User ID : "))
            name = input("Enter Name : ")
            new_user = User(user_id, name)
            library.add_user(new_user)
            print(f"User '{name}' added to Library")

        elif choice == '3':
            library.display_all_books()

        elif choice == '4':
            library.display_all_users()

        elif choice == '5':
            user_id = int(input("Enter the User ID : "))
            book_id = int(input("Enter the Book ID : "))

            user = get_user_by_id(user_id)
            book = get_book_by_id(book_id)

            if user and book:
                library.borrow_book(user, book)
            else:
                print("User or Book not found.")
        elif choice == '6':
            user_id = int(input("Enter the User ID : "))
            book_id = int(input("Enter the Book ID : "))

            user = get_user_by_id(user_id)
            book = get_book_by_id(book_id)

            if user and book:
                library.return_book(user, book)
            else:
                print("User or Book not found.")
        elif choice == '0':
            print("Exiting the Library.")
            break

        else:
            print("Invalid Input")

main()