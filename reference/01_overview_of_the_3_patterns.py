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

# GENERAL IDEA OF Chapter 16:
# Three design patterns in how classes interact:
'''
    ASSOCIATION (the umbrella term)
    An instance variable of one class holds an object of another class:
        1. Aggregation
            You define 2 classes, have 1 object (or more) from each class.
            In one class you store an EXISTING object in an instance variable of a different object
            The 2 objects are related, but independent.

        2. Composition 
            You define 2 classes. In one class you CREATE a new object of another class IN the 1st class's constructor
            The object you created only exists as part of the first class.

    INHERITANCE

        3. Inheritance 
            You have a super class (aka a parent class) and a sub class (the child class)
            The child class gets any variables and methods from the parents,
            but can customize (override) any methods or variables from the parent.
'''

#########
# AGGREGATION
#########
'''
2 separate objects. One gets stored in the other
'''

class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self, list_of_books):
        self.list_of_books = list_of_books  # Library has-a list of Book objects

# Instantiation
book1 = Book("Fahrenheit 451") # book object
book2 = Book("Brave New World") # book object
list_of_books = [book1, book2]
library = Library(list_of_books) # creating a Library object. It contains book objects

# Key point:
# I can still access the original book data:
print(book1.title)

# But I can also access the book through the library object:
print(library.list_of_books[0].title)


#########
# COMPOSITION
#########

'''
1 object is created inside of the other. The inner object can only be accessed
through the outer object.
'''
import random as r

class LibraryCard:
    def __init__(self, card_number):
        self.card_number = card_number

class LibraryMember:
    def __init__(self, name):
        self.name = name
        self.library_card = LibraryCard(r.randint(1,100000)) 

# Instantiation
# LibraryMember is created, but notice that a LibraryCard will be created inside!
member = LibraryMember("Bob") 

# That means I can ONLY access the LibraryCard object THROUGH the LibraryMember object
print(member.name)  # Bob
print(member.library_card.card_number) # 

# This wouldn't work:
#print(library_card.card_number)


#########
# INHERITANCE
#########

'''
1 object is created inside of the other. The inner object can only be accessed
through the outer object.
'''

class LibraryMember:
    def __init__(self, name):
        self.name = name

    def describe_role(self):
        return f"{self.name} is a library member."

class Librarian(LibraryMember):  # Inherits from LibraryMember
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

    def describe_role(self):
        return f"{self.name} is a librarian with employee ID: {self.employee_id}."

# Instantiation
member = LibraryMember("Bob")
librarian = Librarian("Alice", "001")
list_of_members_and_librarians = [member, librarian]

# Inheritance allows for the concept of "polymorphism". 
# describe_role has different logic depending on if the parent or child calls it, but it has the same name.
for object in list_of_members_and_librarians:
    print(object.describe_role())

