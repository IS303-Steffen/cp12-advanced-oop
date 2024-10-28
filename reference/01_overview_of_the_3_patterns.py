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

# ====================================
# OVERVIEW OF 3 OBJECT DESIGN PATTERNS
# ====================================

'''
OVERVIEW
--------
There are 3 main design patterns of how classes interact:


ASSOCIATION (the umbrella term)
-------------------------------
An instance variable of one class holds an object of another class:

1. Aggregation
    - You define 2 classes, have 1 object (or more) from each class.
    - In one class you store an EXISTING object in an instance variable of a
      different object.
    - The 2 objects are related, but independent.

2. Composition 
    - You define 2 classes.
    - In one class you CREATE a new object of another class INSIDE the 1st
      class's (often in the constructor).
    - The object you created only exists as part of the first class.

INHERITANCE
-----------

3. Inheritance 
    - You have a super class (aka the parent class) and a sub class (the child
      class).
    - The child class gets all variables and methods from the parents,
      but can customize (override) any methods or variables from the parent.


You can see brief examples of all three below
'''


# ===================
# AGGREGATION EXAMPLE
# ===================

'''
Notice the Book objects are created before being put in the Library object.
'''

class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self, list_of_books):
        self.list_of_books = list_of_books  # Library has-a list of Book objects

book1 = Book("Fahrenheit 451") # book object
book2 = Book("Brave New World") # book object
list_of_books = [book1, book2]
library = Library(list_of_books) # creating a Library object. It contains book objects

''' KEY POINT: I can still access the original book data: '''
print(book1.title)

''' BUT, I can also access the book through the library object: '''
print(library.list_of_books[0].title)


# ===========
# COMPOSITION
# ===========

'''
Notice LibraryCard object is created INSIDE the LibraryMember class. It can
only be accessed through LibraryMember.
'''
import random as r

class LibraryCard:
    def __init__(self, card_number):
        self.card_number = card_number

class LibraryMember:
    def __init__(self, name):
        self.name = name
        self.library_card = LibraryCard(r.randint(1,100000)) 

member = LibraryMember("Bob") 

''' You get to the LibraryCard through the LibraryMember '''
print(member.name)  # Bob
print(member.library_card.card_number) # 

''' This wouldn't work '''
#print(library_card.card_number)


# ===========
# INHERITANCE
# ===========

'''
Notice that Librarian has LibraryMember in parentheses next to its class 
definition.
'''

class LibraryMember:
    library_name = "Provo Library"

    def __init__(self, name):
        self.name = nameß

    def describe_role(self):
        return f"{self.name} is a library member."

class Librarian(LibraryMember):  # Inherits from LibraryMember
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

    def describe_role(self):
        return f"{self.name} is a librarian with employee ID: {self.employee_id}."

''' Creating an instance of the parent class and the child class '''
member = LibraryMember("Bob")
librarian = Librarian("Alice", "001")

''' notice I'm accessing variables from the parent in the child, even though
    the child never had them created '''
print(librarian.library_name)

list_of_members_and_librarians = [member, librarian]

''' Inheritance allows for the concept of "polymorphism". 
    describe_role has different logic depending on if the parent or child calls
    it, but it has the same name. '''
for object in list_of_members_and_librarians:
    print(object.describe_role())

