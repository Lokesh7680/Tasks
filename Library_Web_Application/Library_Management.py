from flask import Flask, render_template, request, redirect, url_for
import psycopg2 as pg

app = Flask(__name__)

class Book:
    def __init__(self, book_id, title, author, genre):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = True

    def display_details(self):
        return f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Available: {'Yes' if self.available else 'No'}"

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

    def display_details(self):
        return f"User ID: {self.user_id}, Name: {self.name}, Borrowed Books: {len(self.borrowed_books)}"

class Library(Book, User):
    def __init__(self, dbname='Books', user='postgres', password='Harikareddy@1'):
        self.books = []
        self.users = []
        self.conn = pg.connect(dbname=dbname, user=user, password=password)
        # cur = self.conn.cursor()
        # cur.execute('''alter table books add column available boolean default true''')
        # self.conn.commit()
        # cur.close()
        self.fetch_books_from_db()
        self.fetch_users_from_db()

    def fetch_books_from_db(self):
        cur = self.conn.cursor()
        cur.execute('select * from books')
        rows = cur.fetchall()
        cur.close()

        for row in rows:
            book = Book(book_id=row[0], title=row[1], author=row[2], genre=row[3])
            self.books.append(book)

    def fetch_users_from_db(self):
        cur = self.conn.cursor()
        cur.execute('select user_id , name from users')
        rows = cur.fetchall()
        cur.close()

        for row in rows:
            user = User(user_id=row[0], name=row[1])
            self.users.append(user)

    def add_book(self, book):
        self.books.append(book)
        cur = self.conn.cursor()
        cur.execute('''
            INSERT INTO books (book_id, title, author, genre)
            VALUES (%s, %s, %s, %s)
        ''', (book.book_id, book.title, book.author, book.genre))

        self.conn.commit()
        cur.close()

    def add_user(self, user):
        self.users.append(user)
        cur = self.conn.cursor()
        cur.execute('''
                    INSERT INTO users (user_id,name)
                    VALUES(%s,%s)
                    ''', (user.user_id, user.name))

        self.conn.commit()
        cur.close()

    def display_all_books(self):
        return [book.display_details() for book in self.books]

    def display_all_users(self):
        return [user.display_details() for user in self.users]

    def borrow_book(self, user, book):
        if book.available:
            book.available = False
            user.borrowed_books.append(book.book_id) 
            cur = self.conn.cursor()
            cur.execute('''
                UPDATE books
                SET available = FALSE
                WHERE book_id = %s
            ''', (book.book_id,))
            self.conn.commit()
            cur.execute('''
                UPDATE users
                SET borrowed_books = %s
                WHERE user_id = %s
            ''', (user.borrowed_books, user.user_id))
            self.conn.commit()
            cur.close()
            return f"Successfully borrowed {book.title} by {book.author}"
        else:
            return f"Sorry, {book.title} is not available for borrowing"

    def return_book(self, user, book):
        if book.book_id in user.borrowed_books:
            book.available = True
            user.borrowed_books.remove(book.book_id)
            cur = self.conn.cursor()
            cur.execute('''
                UPDATE books
                SET available = TRUE
                WHERE book_id = %s
            ''', (book.book_id,))
            cur.execute('''
                UPDATE users
                SET borrowed_books = %s
                WHERE user_id = %s
            ''', (user.borrowed_books, user.user_id))
            self.conn.commit()
            cur.close()
            return f"Successfully returned {book.title} by {book.author}"
        else:
            return f"Error: {user.name} has not borrowed {book.title}"
        
    # def get_user_by_id(library, user_id):
    #     for user in library.users:
    #         if user.user_id == user_id:
    #             return user
    #     return None

    # def get_book_by_id(library, book_id):
    #     for book in library.books:
    #         if book.book_id == book_id:
    #             return book
    #     return None


def get_user_by_id(library, user_id):
    for user in library.users:
        if user.user_id == user_id:
            return user
    return None

def get_book_by_id(library, book_id):
    for book in library.books:
        if book.book_id == book_id:
            return book
    return None

library = Library(dbname='Books', user='postgres', password='Harikareddy@1')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_book', methods=['GET', 'POST'])
def add_book_form():
    if request.method == 'POST':
        book_id = request.form['book_id']
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']

        new_book = Book(book_id=book_id, title=title, author=author, genre=genre)
        library.add_book(new_book)

        return redirect(url_for('display_all_books'))

    return render_template('add_book.html')

@app.route('/add_user', methods=['GET', 'POST'])
def add_user_form():
    if request.method == 'POST':
        user_id = request.form['user_id']
        name = request.form['name']

        new_user = User(user_id=user_id, name=name)
        library.add_user(new_user)

        return redirect(url_for('display_all_users'))

    return render_template('add_user.html')

@app.route('/display_all_books')
def display_all_books():
    return render_template('display_all_books.html', books=library.display_all_books())

@app.route('/display_all_users')
def display_all_users():
    return render_template('display_all_users.html', users=library.display_all_users())

@app.route('/borrow_book', methods=['GET', 'POST'])
def borrow_book_form():
    if request.method == 'POST':
        user_id = request.form['user_id']
        book_id = request.form['book_id']

        user = get_user_by_id(library, int(user_id))
        book = get_book_by_id(library, int(book_id))

        if user and book:
            result = library.borrow_book(user, book)
            return render_template('result.html', result=result)
        else:
            return render_template('result.html', result="User or book not found.")

    return render_template('borrow_book.html')

@app.route('/return_book', methods=['GET', 'POST'])
def return_book_form():
    if request.method == 'POST':
        user_id = request.form['user_id']
        book_id = request.form['book_id']

        user = get_user_by_id(library, int(user_id))
        book = get_book_by_id(library, int(book_id))

        if user and book:
            result = library.return_book(user, book)
            return render_template('result.html', result=result)
        else:
            return render_template('result.html', result="User or book not found.")

    return render_template('return_book.html')

if __name__ == '__main__':
    app.run(debug=True)
