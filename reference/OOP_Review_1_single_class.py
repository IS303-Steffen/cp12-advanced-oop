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
make a Person class
    Instance variables: name, hobby

    Methods:
        __init__ (the constructor)
        introduce_yourself
            print out "hello, my name is name and my hobby is hobby"

Make two Person objects. run the introduce_yourself method on both of them.

'''

class Person: # name of the class
    def __init__(self, name, hobby): # self MUST come first, then any other parameters you want to pass in
        self.name = name # instance variable
        self.hobby = hobby # instance variable

    def introduce_yourself(self): # method. Self MUST be a parameter
        print(f"Hello, my name is {self.name} and my hobby is {self.hobby}") # get to the instance parameters by referencing self.


person1 = Person("Jim", "Basketball")
person2 = Person("Jenny", "Cycling")


person1.introduce_yourself()
# if it makes it easier to understand what self is, the above is the same as doing this:
Person.introduce_yourself(person1)

person2.introduce_yourself()