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
# COMPOSITION - OBJECT PASSED INTO ANOTHER OBJECT
# ===============================================

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


# PART 2: DESIGN THE LIBARARY MEMBER CLASS
# Create a LibraryMember class. member's name and a LibraryCard object.
# When a LibraryMember object is instantiated, it should automatically create a
# LibraryCard object within it demonstrating the principle of composition.

# Make a LibraryMember object, and try to print out their library card id.



# PART 3: IMPLEMENT CARD VALIDITY CHECK
# Add a method in the LibraryMember class to check whether the member's
# library card is still valid by comparing the current date to the valid_until
# date of the LibraryCard. Print out if it is still valid or not and when it
# expires.

# Try to run the method you wrote on any LibraryMember objects you made.




