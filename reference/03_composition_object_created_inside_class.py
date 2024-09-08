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

# Composition Follow-along Practice
# Practice composition by having library members object own library card objects
# Each library member should have a unique library card that includes an expiration date

'''
Part 1:
    Design the LibraryCard Class:
    This class should include two attributes:
        card_number (you can just make this a random number),
        valid_until (a date indicating when the card expires)
            valid_until date should be calculated from the current date to be valid for a year.

            You can use this code for the valid_until date:
                from datetime import datetime, timedelta
                datetime.today() + timedelta(days=365)

    You can have card_number and valid_until passed as parameters
    to the constructor, or just set the instance variables directly. You choose.

Part 2:
    Design the LibraryMember Class:
    Create a class representing a library member. This class should include the
    member's name and a LibraryCard object.
    When a LibraryMember object is instantiated, it should automatically create a LibraryCard object within it
    demonstrating the principle of composition.

    Make a LibraryMember object, and try to print out their library card id.

Part 3: 
    Implement Card Validity Check:
    Add a method in the LibraryMember class to check whether the member's library card
    is still valid by comparing the current date to the valid_until date of the LibraryCard.
    Print out if it is still valid or not and when it expires.

    Try to run the method you wrote on any LibraryMember objects you made.
'''


from datetime import datetime, timedelta
import random as r

class LibraryCard:
    def __init__(self, card_number, valid_until):
        self.card_number = card_number
        self.valid_until = valid_until

class LibraryMember:
    def __init__(self, name):
        self.name = name
        self.library_card = LibraryCard(r.randint(1, 100000), datetime.today() + timedelta(days=365)) # Valid for 1 year

    def check_card_validity(self):
        if self.library_card.valid_until >= datetime.today():
            print(f"{self.name}'s library card is valid until {self.library_card.valid_until}.")
        else:
            print(f"{self.name}'s library card has expired on {self.library_card.valid_until}.")


# Example Use
member = LibraryMember("Bob")
print(member.library_card.card_number)
member.check_card_validity()  # Check if Bob's card is valid





