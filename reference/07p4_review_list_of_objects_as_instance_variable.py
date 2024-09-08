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
Do the same as the previous, but now DogPerson's dog variable should now be dog_list, which should initially be an empty list.
    Note: you should make the empty list in the constructor, not in the list of parameters.

Alter Dog to include a method called dog_info.
    - it should print out "name, breed"

Alter DogPerson's introduce_yourself. If they have at least one dog, say:
    "Hello, my name is name and my hobby is hobby and these are my dogs:"
        then run dog_info on each of their dogs.
    
    But if they have no dogs, print out:
    "Hello, my name is name and my hobby is hobby but I don't have a dog yet!"

Make a dogPerson, and add 3 dogs to their list.
Make another dogPerson, but don't add any dogs to their list.
run introduce_yourself on both
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

dog_person = DogPerson("Jimmy", "Basketball")
dog_person2 = DogPerson("Samantha", "Tennis")

#add three dogs to dog_person's list:
dog_person.dog_list.append(dog1)
dog_person.dog_list.append(dog2)
dog_person.dog_list.append(dog3)


dog_person.introduce_yourself()
dog_person2.introduce_yourself()