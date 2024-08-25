import tkinter as tk
from tkinter import messagebox

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False

    def __str__(self):
        status = 'Borrowed' if self.is_borrowed else 'Available'
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books and book.return_book():
            self.borrowed_books.remove(book)
            return True
        return False

    def __str__(self):
        return f"{self.name} (ID: {self.member_id})"


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        book_to_remove = None
        for book in self.books:
            if book.isbn == isbn:
                book_to_remove = book
                break

        if book_to_remove:
            self.books.remove(book_to_remove)
            return True
        else:
            return False

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member_id):
        member_to_remove = None
        for member in self.members:
            if member.member_id == member_id:
                member_to_remove = member
                break

        if member_to_remove:
            self.members.remove(member_to_remove)
            return True
        else:
            return False

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def list_available_books(self):
        return [book for book in self.books if not book.is_borrowed]

    def list_borrowed_books(self):
        return [book for book in self.books if book.is_borrowed]

    def list_members(self):
        return self.members


class LibraryGUI:
    def __init__(self, root):
        self.library = Library()
        self.root = root
        self.root.title("Library Management System")

        # Add Book Frame
        self.add_book_frame = tk.Frame(self.root)
        self.add_book_frame.pack(pady=10)

        tk.Label(self.add_book_frame, text="Title:").grid(row=0, column=0)
        self.book_title_entry = tk.Entry(self.add_book_frame)
        self.book_title_entry.grid(row=0, column=1)

        tk.Label(self.add_book_frame, text="Author:").grid(row=1, column=0)
        self.book_author_entry = tk.Entry(self.add_book_frame)
        self.book_author_entry.grid(row=1, column=1)

        tk.Label(self.add_book_frame, text="ISBN:").grid(row=2, column=0)
        self.book_isbn_entry = tk.Entry(self.add_book_frame)
        self.book_isbn_entry.grid(row=2, column=1)

        self.add_book_button = tk.Button(self.add_book_frame, text="Add Book", command=self.add_book)
        self.add_book_button.grid(row=3, columnspan=2)

        # Add Member Frame
        self.add_member_frame = tk.Frame(self.root)
        self.add_member_frame.pack(pady=10)

        tk.Label(self.add_member_frame, text="Member Name:").grid(row=0, column=0)
        self.member_name_entry = tk.Entry(self.add_member_frame)
        self.member_name_entry.grid(row=0, column=1)

        tk.Label(self.add_member_frame, text="Member ID:").grid(row=1, column=0)
        self.member_id_entry = tk.Entry(self.add_member_frame)
        self.member_id_entry.grid(row=1, column=1)

        self.add_member_button = tk.Button(self.add_member_frame, text="Add Member", command=self.add_member)
        self.add_member_button.grid(row=2, columnspan=2)

        # List Books Button
        self.list_books_button = tk.Button(self.root, text="List Available Books", command=self.list_books)
        self.list_books_button.pack(pady=5)

        # List Members Button
        self.list_members_button = tk.Button(self.root, text="List Members", command=self.list_members)
        self.list_members_button.pack(pady=5)

        # Quit Button
        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.quit)
        self.quit_button.pack(pady=20)

    def add_book(self):
        title = self.book_title_entry.get()
        author = self.book_author_entry.get()
        isbn = self.book_isbn_entry.get()
        book = Book(title, author, isbn)
        self.library.add_book(book)
        messagebox.showinfo("Success", f"Book '{title}' added successfully!")

    def add_member(self):
        name = self.member_name_entry.get()
        member_id = self.member_id_entry.get()
        member = Member(name, member_id)
        self.library.add_member(member)
        messagebox.showinfo("Success", f"Member '{name}' added successfully!")

    def list_books(self):
        available_books = self.library.list_available_books()
        if available_books:
            books = "\n".join(str(book) for book in available_books)
        else:
            books = "No available books."
        messagebox.showinfo("Available Books", books)

    def list_members(self):
        members = self.library.list_members()
        if members:
            members_list = "\n".join(str(member) for member in members)
        else:
            members_list = "No members found."
        messagebox.showinfo("Library Members", members_list)


if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryGUI(root)
    root.mainloop()
