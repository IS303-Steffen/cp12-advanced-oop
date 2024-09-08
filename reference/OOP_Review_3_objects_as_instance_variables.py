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
Do the same as the previous, but make a Dog class
    - Instance variables: Name, Breed
    - methods:
        - __init__() (the constructor)

        
Now, instead of a DogPerson's dog variable holding a string, make it hold a Dog object.
Alter DogPerson's introduce_yourself to say "Hello, my name is name and my hobby is and and my dog name is a breed"

Make a Dog
Make a DogPerson, and then run introduce_yourself on that DogPerson

'''



class Person: # name of the class
    def __init__(self, name, hobby): # self MUST come first, then any other parameters you want to pass in
        self.name = name # instance variable
        self.hobby = hobby # instance variable

    def introduce_yourself(self): # method. Self MUST be a parameter
        print(f"Hello, my name is {self.name} and my hobby is {self.hobby}") # get to the instance parameters by referencing self.


# make your DogPerson class here
class DogPerson(Person):
    def __init__(self, name, hobby, dog):
        super().__init__(name, hobby)
        self.dog = dog

    def introduce_yourself(self):
        print(f"Hello, my name is {self.name} and my hobby is {self.hobby} and my dog {self.dog.name} is a {self.dog.breed}")

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


dog = Dog("Max", "Golden Retriever")

dog_person = DogPerson("Jimmy", "Basketball", dog)

dog_person.introduce_yourself()
