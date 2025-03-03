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

# ===================
# GETTERS AND SETTERS
# ===================

'''
OVERVIEW
--------
Whenever you have a private variable, the way to give access to the variable
outside of the class (or in an inherited class) is to create a method that
just returns that private variable (called a getter) and a method that sets
a new value for a private variable (called a setter).
'''

class User:
    def __init__(self, user_id: str):
        self.__id = None  # Initialize truly private variable
        self.set_id(user_id)  # Use setter for validation

    def get_id(self):
        """Getter method for retrieving the user ID."""
        return self.__id

    def set_id(self, new_id):
        """Setter method for validating and setting the user ID."""
        if not isinstance(new_id, str) or len(new_id) != 8:
            raise ValueError("User ID must be an 8-character string.")
        self.__id = new_id

# 1. ADDING A GETTER AND A SETTER
# Make the id instance variable private. Then create a method called "get_id"
# that will return the id. Then also create a method called "set_id" that will
# set a new id as long as it is a string that is exactly 8 characters long.

try:
    user = User("abc12345")  # Valid ID
    print(user.get_id())  # Output: abc12345
    
    user.set_id("Invalid User ID!")  # This will raise ValueError
except ValueError as e:
    print(e)

# Attempt to access private variable directly (will fail)
try:
    print(user.__id)  # AttributeError: 'User' object has no attribute '__id'
except AttributeError as e:
    print(e)



'''
TIP:
----

When doing some kind of data validation, like in the above example, if the 
requirements for the variable aren't met (like it must be example 8 characters
long, etc.) you can raise an error, like this:

if len(my_input): != 8
    raise ValueError("The user id must be exactly 8 characters long")

'''