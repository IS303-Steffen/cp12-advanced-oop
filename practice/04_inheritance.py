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

# GENERAL IDEA OF Chapter 16:
# classes can interact in 3 ways (basically)
'''
    Instance variable of a class is an object:
        1. You define 2 classes. In one class you PASS an existing object into the constructor
            The 2 objects are related, but independent.

        2. You define 2 classes. In one class you CREATE a new object in the constructor
            The object you created only exists as part of the first class.

    Class inheritance

        3. You have a super class (like a father or mother class) and a sub class (the child class)
            The child class gets any variables and methods from the parents, but can customize (override) any methods or variables from the parent.

'''


# This is an example of #3. We have an Employee and a Manager.
# A Manager is also an Employee, but a more specific type of Employee.

# Main things to remember:
'''
    1. Super class is the parent

    2. Sub class is the child

    3. To specify a super class, put the class name in parentheses.
        - class Manager(Employee):

    4. Sub class gets access to all class variables and methods from the super class

    5. If you write a method or variable in the SUB class that has the same name
        as the SUPER class, the SUB class will OVERRIDE the super class. This is also called polymorphism.

    6. If you are:
            1: in a sub class
            2: are in a method that is overwritten (has the same name as method in the super class)
            3: want to call the super class version of that method instead of the sub class version
        THEN:
            you can use super().methodName() to call the method of the super class

    6.1 IMPLICATION FOR __init__
        every class calls __init__ whether you write it out or not. If you want the sub class
        to have the same instance variables as the super class, you must call super().__init__(self, any other variables)

'''

# Inheritance Follow-along Practice
# You'll create classes for Employees and Managers, with Managers inheriting from Employees


'''
PART 1:
Write an employee class:
    class variable:
        company_name
    
    instance variables:
        name
        salary
    
    methods:
        - constructor
        - get_status: returns or prints what their name is and their salary
        - give_raise: increase their salary by a passed in amount

    create an employee object, and run get_status and give_raise

'''


'''
PART 2:

write a Manager class that inherits from employee

    methods:
        - constructor: override the constructor, call the employee constructor through super(). 
                managers should also have an instance variable for "department" to show which department they are managing.

        - give_raise: override the inherited version. Make it so that managers can also get a bonus, which is a default of 10% added to whatever
                        the raise amount is.
                Note: if we have time, discuss using or not using super() in a situation like this.

        - give_praise: a method that only exists for the manager. Recieves an employee object and then just says "You're doing great, {employee name}"


create a manager object and run all the relevant methods on it. Make sure that when giving it a raise, it also gets the increased amount.
'''

