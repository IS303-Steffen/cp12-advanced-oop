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
Implementing a Vehicle Hierarchy in Python

Step 1: Define the Base Class Vehicle
Create a class named Vehicle. This class will serve as the base class for all vehicle types.
Add an __init__ method. This method should initialize the make, model, and year attributes.
Implement a start method. This method should print a message indicating that the vehicle has started.
Implement a stop method. This method should print a message indicating that the vehicle has stopped.
'''

'''
Step 2: Create Derived Classes for Different Vehicle Types
Create a class named Car that inherits from Vehicle.
    You don't need to add any new methods or attributes for this class yet.
    Just make sure it inherits the properties and methods from Vehicle. (you can use the keyword "pass" after the class name)

Create a class named Truck that also inherits from Vehicle.
    Add a new attribute named cargo_capacity to the __init__ method, which represents the cargo capacity of the truck.
    Override the start method to include a message that also mentions the cargo capacity when the truck starts.

Create a class named Motorcycle that inherits from Vehicle.
    Add a new method named rev_engine, which prints a message indicating the motorcycle's engine is revving.
'''

'''
Step 3: Test Your Vehicle Hierarchy
Instantiate an object of each vehicle class (Car, Truck, Motorcycle) with appropriate attributes.

Call the start and stop methods on each of your vehicle objects.
Call the rev_engine method on your motorcycle object.
Print the make, model, and year of each vehicle.
'''