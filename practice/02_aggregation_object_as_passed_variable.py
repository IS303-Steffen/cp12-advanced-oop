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

# Aggregation Follow-along Practice
# You'll create a simple library system where library members can check out books.
# You will practice aggregation by having LibraryMember objects maintain a list of Book objects they have checked out


'''
PART 1: Define the Book Class
    Create the Book Class: Start by defining a Book class with a constructor (__init__ method).
    Each book should have title and author attributes passed as arguments to the constructor.
    Add Availability Attribute: Include an is_available attribute that tracks whether the book is available for checkout.
    Initialize it to True in the constructor.

    Create at least three Book objects with different titles and authors to test your class.
'''

'''
PART 2: Define the LibraryMember Class
    Create the LibraryMember Class: Define a LibraryMember class with a constructor that accepts a name as an argument.
    Add Checked Out Books Attribute: Include an attribute to store a list of books that the member
    has checked out. Initialize it as an empty list.

    Create at least two LibraryMember objects.
'''

'''
Step 3: Implement Checkout Logic
Implement checkout_book Method:
    Add a checkout_book method to the LibraryMember class. This method should accept
    a Book object as an argument.

    Within the checkout_book method do 2 checks:
        1. Verify if the book is available (is_available is True).
            If the book is not available, print a message indicating it cannot be checked out.
        2. Ensure that a member cannot check out more than 3 books. If attempting to check out more, print an appropriate message.

    If the book is available and the member has not exceeded the limit, mark the book as not available (is_available = False),
    and add it to the member's list of checked out books.
    
    Add some book object's to a LibraryMember's book list and try looping through the list of books of a LibraryMember and printing out their title
'''

'''
Step 4: Implement Return Logic
    Implement return_book Method:
    Add a return_book method to the LibraryMember class that accepts a Book object as an argument.
    Update Book and Member Status: If the book is in the member's list of checked out books,
    remove it from the list and mark it as available (is_available = True).

    Test the Return Logic: Test returning books to ensure that books can be successfully returned and checked out again.
'''








