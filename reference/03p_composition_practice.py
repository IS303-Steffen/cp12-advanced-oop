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

# ======================
# COMPOSITION - PRACTICE
# ======================

# 1. PRACTICE
# Your task is to model a simple relationship between animals and their
# heartbeats.

# PART 1. Heart Class:
#   - Create a class named `Heart`.
#   - Add an attribute `beats_per_minute` with a default value of 70.
#   - Define a method named `beat` within this class. This method should return
#     the string "Thump thump!" when called.

# PART 2. Animal Class:
#   - Create another class named Animal.
#   - This class should have an __init__ method that accepts a parameter
#     species
#   - Within the __init__ method, instantiate the Heart class (e.g. call the
#     Heart class) and assign it to an instance variable named heart.
   

class Animal:
    def __init__(self, species):
        self.species = species
        self.heart = Heart()

class Heart:
    def __init__(self):
        self.beats_per_minute = 70
   
    def beat(self):
        return "thump thump!"

# PART 3. Using the Classes:
#   - Instantiate the `Animal` class with the species "Dog".
#   - Print the species of the created animal.
#   - Print the `beats_per_minute` attribute of the animal's heart.
#   - Print the result of the `beat` method of the animal's heart.

animal_object = Animal("Dog")
print(animal_object.species)

print(animal_object.heart.beats_per_minute)
animal_object.heart.beat()


