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

# ====================
# INHERITANCE PRACTICE
# ====================


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
book_5 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book_6 = Book("Crime and Punishment", "Fyodor Dostoevsky")
book_7 = Book("Jane Eyre", "Charlotte Brontë")
book_8 = Book("Wuthering Heights", "Emily Brontë")
book_9 = Book("The Odyssey", "Homer")
book_10 = Book("To Kill a Mockingbird", "Harper Lee")


# YOUR TASK:
# Create a new class PremiumLibraryMembers that inherits from LibraryMember
# class variabes:
#   starting_check_out_limit = 3
# instance variables:
#   - all those from LibraryMembers
#   - check_out_limit (should be equal to starting_check_out_limit)
#   - all_time_num_checked_out (should be 0 to start)
#
# Make it so that when PremiumLibraryMembers check out a book, it uses
# their check_out_limit instead of the default 2 that normal LibraryMembers
# have. It should also update the all_time_num_checked_out number each time
# they succesfully check out a book.
# Create a PremiumLibraryMember and show that they can check out
# 3 books instead of just 2.

# BONUS IMPROVEMENTS
# 1. Can you figure out a way to write check_out_book so that you dont repeat
#    nearly all the code from LibraryMember in PremiumLibraryMember? Some ideas
#    would be using super(), probably with either an extra parameter, or using
#    a function like getattr() (look it up!)
#
# 2. Add a method to PremiumLibraryMember called calculate_check_out_limit that
#    increases the check_out_limit by one each time a PremiumLibraryMember
#    checks out 4 books (so if they have checked out 4 their limit should be 4,
#    if they've checked out 8 their limit should be 5, if they've checked out
#    12 their limit should be 6, etc.)


