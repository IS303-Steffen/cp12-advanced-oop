# optional stuff that will clear the window each time you run it.
import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

###########################
# START READING HERE
###########################

### Inheritance Practice

'''
You are given this code for Books and LibraryMembers:
'''

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
        if len(self.checked_out_books) >= 3:
            print(f"{self.name} cannot check out more than 3 books.")
        elif book.is_available is False:
            print(f"The book '{book.title}' is currently not available.")
        else:
            book.is_available = False
            self.checked_out_books.append(book)
            print(f"{self.name} has checked out '{book.title}'.")

    def return_book(self, book):
        if book in self.checked_out_books:
            book.is_available = True
            self.checked_out_books.remove(book)
            print(f"{self.name} has returned '{book.title}'.")
        else:
            print(f"{self.name} cannot return a book they haven't checked out.")

'''
YOUR TASK:
Create a new class called PremiumLibraryMembers.
They should be the same as LibraryMembers, except they also have an instance variable called
"check_out_limit". The default is 5, but can be increased beyond that potentially.

This means that when they try to check out a book, they should use their check_out_limit variable as the limit
instead of the standard 3 that is applied to normal Library Members.

Write the functionality for this and make a LibraryMember and PremiumLibraryMember object to test the functionality.
'''

class PremiumLibraryMember(LibraryMember):
    def __init__(self, name, check_out_limit=5):
        super().__init__(name)
        self.check_out_limit = check_out_limit

    def check_out_book(self, book):
        if len(self.checked_out_books) >= self.check_out_limit:
            print(f"{self.name} cannot check out more than {self.check_out_limit} books.")
        elif book.is_available is False:
            print(f"The book '{book.title}' is currently not available.")
        else:
            book.is_available = False
            self.checked_out_books.append(book)
            print(f"{self.name} has checked out '{book.title}'.")

# Testing functionality
book1 = Book("Python Programming", "Jane Doe")
book2 = Book("Learning Python", "John Smith")
book3 = Book("Advanced Python", "Alex Johnson")
book4 = Book("Python for Data Science", "Maria Garcia")
book5 = Book("Python and Machine Learning", "An Nguyen")
book6 = Book("Introduction to Python", "Bao Tran")

member = LibraryMember("Regular Joe")
premium_member = PremiumLibraryMember("VIP Anna", 7)

# Regular member checking out books
member.check_out_book(book1)
member.check_out_book(book2)
member.check_out_book(book3)
member.check_out_book(book4)  # Should not be allowed

# Premium member checking out books
premium_member.check_out_book(book4)
premium_member.check_out_book(book5)
premium_member.check_out_book(book6)
premium_member.check_out_book(book1)  # Should be allowed as book1 is already checked out and not available

# Returning books
member.return_book(book1)
premium_member.check_out_book(book1)  # Should now be allowed