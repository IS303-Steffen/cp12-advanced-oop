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

# PART 1: DEFINE A BOOK CLASS (GIVEN TO YOU)
# You are provided with a Book class with 3 instance variables:
#   title, author, is_available
# Book instances are already created for you.

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
# Define a LibraryMember class. For now, just make it have instance variables
# of name and checked_out_books. Make name have a corresponding parameter,
# but just set checked_out_books equal to an empty list.
#
# Create two LibraryMember objects. Append a book or two to each
# LibraryMember's checked_out_books list. Print out the title of the first
# book in each LibraryMember's list.


# PART 3: IMPLEMENT CHECK OUT LOGIC
# Add a check_out_book method to the LibraryMember class. This method should
# accept a Book object as an argument. Within the check_out_book method do 2
# checks:
#   1. Verify if the book is available (is_available is True). If the book is
#      not available, print a message indicating it cannot be checked out.
#   2. Ensure that a member cannot check out more than 2 books.
#      If attempting to check out more, print:
#       "<name> cannot check out more than 2 books.""

# If the book is available and the member has not exceeded the limit, mark the
# book as unavailable (is_available = False), and add it to the member's list
# of checked out books. Print out this message:
#   "<name> has checked out '<book title>'. They now have <num checked out>
#    book(s) checked out."



# PART 4: TESTING CHECK_OUT_BOOK
# Comment out the code from Part 2 or clear the LibraryMember's lists before
# doing this. 
# Add some book objects to a LibraryMember's book list until they get a
# message that they can't check out any more books. try looping through
# the list of books of a LibraryMember and printing out their title.
# Then, try checking out a book that has already been checked out to a 
# different LibraryMember



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
