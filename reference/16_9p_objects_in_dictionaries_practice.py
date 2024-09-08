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

# given this Person class and 3 person objects:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
person3 = Person("Charlie", 35)

# 1: Create a dictionary to store the person objects.
#       Use the persons name as the key, and the entire object as the value

person_dictionary = {person1.name : person1, person2.name : person2, person3.name : person3}


# 2: Individually access each of the objects and run their print_info method

person_dictionary["Alice"].print_info()
person_dictionary["Bob"].print_info()
person_dictionary["Charlie"].print_info()

# 3: Loop through the dictionary of people and run the print_info method for each

for person_name in person_dictionary:
    person_dictionary[person_name].print_info()