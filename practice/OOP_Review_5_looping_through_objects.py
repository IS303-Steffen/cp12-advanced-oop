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
Do the same as the previous, but now make 1 Person, and 2 DogPersons. Give the DogPersons some dogs.

Put all the Person and DogPerson objects in a list. Then loop through the list and run introduce_yourself() on each Person/DogPerson

'''


class Person: # name of the class
    def __init__(self, name, hobby): # self MUST come first, then any other parameters you want to pass in
        self.name = name # instance variable
        self.hobby = hobby # instance variable

    def introduce_yourself(self): # method. Self MUST be a parameter
        print(f"Hello, my name is {self.name} and my hobby is {self.hobby}") # get to the instance parameters by referencing self.


# make your DogPerson class here
class DogPerson(Person):
    def __init__(self, name, hobby):
        super().__init__(name, hobby)
        self.dog_list = []

    def introduce_yourself(self):
        if self.dog_list:
            print(f"Hello, my name is {self.name} and my hobby is {self.hobby} and these are my dogs:")
            for dog in self.dog_list:
                dog.dog_info()
        else:
            print(f"Hello, my name is {self.name} and my hobby is {self.hobby} but I don't have a dog yet!")

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def dog_info(self):
        print(f"{self.name}, {self.breed}")


dog1 = Dog("Max", "Golden Retriever")
dog2 = Dog("James", "Husky")
dog3 = Dog("Alice", "Poodle")

person = Person("Nick", "Hanging Out")
dog_person = DogPerson("Jimmy", "Basketball")
dog_person2 = DogPerson("Samantha", "Tennis")

#add three dogs to dog_person's list:
dog_person.dog_list.append(dog1)
dog_person.dog_list.append(dog2)
dog_person.dog_list.append(dog3)

# put all the people in a list:


# loop through the list and run their introduce_yourself method
