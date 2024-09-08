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

Practice problem:
Your task is to model a simple relationship between animals and their heartbeats.

1. Heart Class:
   - Create a class named `Heart`.
   - Add an attribute `beats_per_minute` with a default value of 70.
   - Define a method named `beat` within this class. This method should return the string "Thump thump!" when called.
'''

'''
2. Animal Class:
   - Create another class named Animal.
   - This class should have an __init__ method that accepts a parameter species
   - Within the __init__ method, instantiate the Heart class (e.g. call the Heart class)
      and assign it to an instance variable named heart.
   
'''

'''
3.Using the Classes:
   - Instantiate the `Animal` class with the species "Dog".
   - Print the species of the created animal.
   - Print the `beats_per_minute` attribute of the animal's heart.
   - Print the result of the `beat` method of the animal's heart.
'''



