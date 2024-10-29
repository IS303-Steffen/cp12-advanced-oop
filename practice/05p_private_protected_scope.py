import os
import platform

def clear_screen():
    """
    Clears the terminal screen to make it easier to follow along with code.
    """
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

# ==================================
# PRIVATE & PROTECTED SCOPE PRACTICE
# ==================================

# 1. PRACTICE:
# You are given this code for Books and LibraryMembers:

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

class LibraryMember:
    def __init__(self, name):
        self.name = name
        self.checked_out_books = []

    def check_out_book(self, book):

        limit = 2

        if len(self.checked_out_books) >= limit:
            print(f"{self.name} cannot check out more than {limit} books.")
        elif book.is_available is False:
            print(f"The book '{book.title}' is currently not available.")
        else:
            book.is_available = False
            self.checked_out_books.append(book)
            print(f"{self.name} has checked out '{book.title}'. They now have {len(self.checked_out_books)} book(s) checked out.")

    def return_book(self, book):
        if book in self.checked_out_books:
            book.is_available = True
            self.checked_out_books.remove(book)
            print(f"{self.name} has returned '{book.title}'. They now have {len(self.checked_out_books)} book(s) checked out.")
        else:
            print(f"{self.name} cannot return a book they haven't checked out.")

book_1 = Book("Pride and Prejudice", "Jane Austen")
book_2 = Book("Moby-Dick", "Herman Melville")
book_3 = Book("Great Expectations", "Charles Dickens")
book_4 = Book("War and Peace", "Leo Tolstoy")

james_member = LibraryMember("James")

# this member is checking out 4 books when the limit should be 2
james_member.checked_out_books.append(book_1)
james_member.checked_out_books.append(book_2)
james_member.checked_out_books.append(book_3)
james_member.checked_out_books.append(book_4) 

# 1. CONTINUED
# Notice that `james_member` is adding 4 books to his list, but the logic in
# check_out_book states that there should be a limit of 2 books. How can you
# alter the code so that adding more than 2 is not possible (or at least harder
# than it normally would be)
# 
# Make whatever changes are necessary, and then try to add 3 books to
# `james_member`'s book list. You might need to clear out his list or comment
# out the previously provided code first.


