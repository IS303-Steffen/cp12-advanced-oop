from helper_functions import clear_screen
clear_screen()

# ==================================================
# COMPOSITION - OBJECT CREATED INSIDE ANOTHER OBJECT
# ==================================================

'''
OVERVIEW
--------
Composition is when you make an object of a class INSIDE the object of a
different class.

PRACTICE
--------
# Practice composition by having library members object own library card
# objects. Each library member should have a unique library card that includes
# an expiration date
'''


# PART 1: DESIGN THE LIBRARY CARD CLASS
# LibraryCard class should include two attributes:
#   card_number: (you can just make this a random number),
#   valid_until: (a date indicating when the card expires)
#                 valid_until date should be calculated from the current date
#                 to be valid for a year.
# Use this for the valid_until date:
'''
    from datetime import date, timedelta
    datetime.today() + timedelta(days=365)
'''
# Don't make any LibaryCard objects yet. We are going to make them inside
# the other class soon.

from datetime import date, timedelta
import random as r

class LibraryCard:
    def __init__(self):
        self.card_number = r.randrange(1, 100_001)
        self.valid_until = date.today() + timedelta(days=365)

# PART 2: DESIGN THE LIBARARY MEMBER CLASS
# Create a LibraryMember class. member's name and a LibraryCard object.
# When a LibraryMember object is instantiated, it should automatically create a
# LibraryCard object within it demonstrating the principle of composition.

# Make a LibraryMember object, and try to print out their library card id.

class LibraryMember:
    def __init__(self, name):
        self.name = name
        self.library_card = LibraryCard()

    def check_card_validity(self):
        if self.library_card.valid_until >= date.today():
            print(f"{self.name}'s library card is valid until {self.library_card.valid_until}.")
        else:
            print(f"{self.name}'s library card has expired on {self.library_card.valid_until}.")

# PART 3: IMPLEMENT CARD VALIDITY CHECK
# Add a method in the LibraryMember class to check whether the member's
# library card is still valid by comparing the current date to the valid_until
# date of the LibraryCard. Print out if it is still valid or not and when it
# expires.

# Try to run the method you wrote on any LibraryMember objects you made.

member = LibraryMember("Bob")
print(member.library_card.card_number)
member.check_card_validity()  # Check if Bob's card is valid





