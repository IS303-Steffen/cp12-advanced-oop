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

# ==========
# PROPERTIES
# ==========

'''
OVERVIEW
--------
When working with private variables, instead of creating normal getter and
setter methods, you can create special methods that have "decorators" at the 
top of them. These make the methods act more like traditional variables,
meaning that when you call them, you leave off the parentheses ().

PROPERTY:
---------
Use it to return a variable.

@property
def name(self)
    return name

SETTERS AND DELETERS:
---------------------
If you've set a property, then you can repeat that property function name,
but set it as a setter or a deleter. This will then control what happens when
you try to set or delete a property

@name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            print("Name must be a string")
        self._name = new_name

@name.deleter
def name(self):
    del self._name

'''

# 1. USING PROPERTIES AND SETTERS
# Create a class called Circle. Make it have a private variable called __radius
# make a property called radius that returns __radius. # make a setter called
# radius that will set the value of __radius as long as it is an number greater
# than zero. Also create a property called area that computes the area of
# the circle 3.14159 * self.__radius ** 2 and returns it.
# Make sure that you are calling the setter method when you first create the
# circle to make sure that 


