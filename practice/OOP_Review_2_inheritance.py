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

'''
I'm giving you starting code for the Person.
Make a DogPerson class that inherits from Person.
    - They have the same instance variables, but DogPerson also has a variable called dog, for a string to store a dog name.
        Use super() to call the Person constructor.
    - The method introduce_yourself should be overwritten so that it also says "and my dog's name is dog" at the end.

Make a Person object, then a DogPerson object. call introduce_yourself() on both.
'''

class Person: # name of the class
    def __init__(self, name, hobby): # self MUST come first, then any other parameters you want to pass in
        self.name = name # instance variable
        self.hobby = hobby # instance variable

    def introduce_yourself(self): # method. Self MUST be a parameter
        print(f"Hello, my name is {self.name} and my hobby is {self.hobby}") # get to the instance parameters by referencing self.


# make your DogPerson class here


# make a person and a dogperson.


# run introduce_yourself() on each of the objects.

