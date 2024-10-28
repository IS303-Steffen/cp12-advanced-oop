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

# ===============================================
# AGGREGATION - OBJECT PASSED INTO ANOTHER OBJECT
# ===============================================

'''
OVERVIEW
--------
Aggregation is when you make 2 objects of different classes, and then put
one object inside the other one.

PRACTICE
--------
You'll create a simple library system where library members can check out
books. You will practice aggregation by having LibraryMember objects maintain
a list of Book objects they have checked out
'''

# PART 1: DEFINE A BOOK CLASS
# Create the Book Class: Start by defining a Book class with a constructor
# (__init__ method). Each book should have title and author attributes passed
# as arguments to the constructor. Include an is_available attribute that
# tracks whether the book is available for checkout. Set it equal to True in
# the constructor.

# Create at least three Book objects with different titles and authors to test
# your class.


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

# Create some books
book_1 = Book("1984", "George Orwell")
book_2 = Book("Brave New World", "Aldous Huxley")
book_3 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book_4 = Book("To Kill a Mockingbird", "Harper Lee")


# PART 2: DEFINE THE LIBRARYMEMBER CLASS
# Define a LibraryMember class with a constructor that accepts a name as an
# argument. Include an attribute to store a list of books that the member
# has checked out. Set it equal to an empty list.

# Create at least two LibraryMember objects.


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

# Create a library member
member_alice = LibraryMember("Alice")
member_john = LibraryMember("John")


# PART 3: IMPLEMENT CHECK OUT LOGIC
# Add a check_out_book method to the LibraryMember class. This method should
# accept a Book object as an argument. Within the check_out_book method do 2
# checks:
#   1. Verify if the book is available (is_available is True). If the book is
#      not available, print a message indicating it cannot be checked out.
#   2. Ensure that a member cannot check out more than 3 books.
#      If attempting to check out more, print an appropriate message.

# If the book is available and the member has not exceeded the limit, mark the
# book as not available (is_available = False), and add it to the member's list
# of checked out books.

''' See above for the check_out_method '''

# PART 4: TESTING CHECK_OUT_BOOK
# Add some book objects to a LibraryMember's book list until they get a
# message that they can't check out any more books. try looping through
# the list of books of a LibraryMember and printing out their title.
# Then, try checkign out a book that has already been checked out to a 
# different LibraryMember

member_alice.check_out_book(book_1)  # Should succeed
member_alice.check_out_book(book_2)  # Should succeed
member_alice.check_out_book(book_3)  # Should succeed
member_alice.check_out_book(book_4)  # Should fail (more than 3 books)

for book in member_alice.checked_out_books:
    print(book.title)

member_john.check_out_book(book_2)
member_john.check_out_book(book_4)

''' 
Only do Part 5 if we have time. It makes the LibraryMember class more complete
but doesn't teach any new aggregation concepts.
'''

# PART 5: IMPLEMENT RETURN LOGIC
# Add a return_book method to the LibraryMember class that accepts a Book
# object as an argument. If the book is in the member's list of checked out
# books, remove it from the list and mark it as available
# (is_available = True). Test returning books to ensure that books can be
# successfully returned and checked out again.

# Return a book and try checking out another one
member_alice.return_book(book_2)
member_john.check_out_book(book_2)  # Should now succeed







