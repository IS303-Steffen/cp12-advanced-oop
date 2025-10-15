from helper_functions import clear_screen
clear_screen()

# ===========
# INHERITANCE
# ===========

'''
OVERVIEW
--------
Inheritance is when you have a child class "inherit" variables and methods
from a parent class.

WHY DO THIS?
------------
- Reuse code!
    Let's say you have 2 similar but different classes. If you make them both
    inherit from the same parent class, then you just have to write the code
    that applies to both child classes once.
- Fewer places to update
    Extending the previous example, what if you needed to update the
    functionality of the 2 child classes? Because of inheritance you can just
    update the code in one place (the parent class) and have it apply to the
    children automatically
- Logical Structure!
    If you use inheritance well it can lend itself towards an easier to
    understand structure of your code that mimics real-life logic.

KEY POINTS
----------

1. Super class is the parent

2. Sub class is the child

3. To specify a super class, put the class name in parentheses.
    - class Manager(Employee):

4. Sub class gets access to all variables and methods from the super class.

5. If you write a method or variable in the SUB class that has the same name
    as the SUPER class, the SUB class will OVERRIDE the super class. This is
    referred to as polymorphism.

6. If you are:
    1: in a sub class
    2: are in a method that is overridden (has the same name as method in the
       super class)
    3: want to call the super class version of that method instead of the sub
       class version
    THEN:
        you can use super().methodName() to call the method of the super class

6.1 IMPLICATION FOR __init__
    every class calls __init__ whether you write it out or not. If you want
    the sub class to have the same instance variables as the super class,
    you must call super().__init__(self, any other variables)

PRACTICE
--------
We have an Employee and a Manager. A Manager is also an Employee, but a more
specific type of Employee.
'''


# PART 1: DEFINE AN EMPLOYEE CLASS
# class variable:
#   company_name
#
# instance variables:
#   name
#   salary
#
# methods:
#   constructor
#   get_status: returns their name and their salary
#   give_raise: increase their salary by a passed in amount. If a raise over
#               20k is given, limit the raise amount to just 20k
#     
# Create an employee object, and run get_status and give_raise



# PART 2.1: DEFINE A MANAGER CLASS
# Write a Manager class that inherits from Employee. Just put "pass" the line
# after "class" and don't put anything else in the class. Then create a 
# Manager object and try to access a variable or method from Employee.

'''
TIP
---
pass is a statement in Python that does literally nothing. It is nice sometimes
when syntactically you are required to have a line of code after a colon
such as after defining a class name, after an if statement, etc. But you don't
want to write that piece of code yet.
'''



# PART 2.2: EXTEND: ADD NEW METHOD
# In the Manager class, add a method that only exists for the manager called
# give_praise. Put a paramater in for an employee object. The method should
# just return a string that says "You're doing great, <employee name>!"
# Create a Manager object and call give_prase
''' method added above'''

# PART 2.3: CUSTOMIZE: OVERRIDE EXISTING METHOD
# In the Manager class, add a method called give_raise (the same name as the
# method in the Employee class). However, managers get a 10% bonus to whatever
# raise is given to them (but they are still subject to the 20k cutoff).
# Discuss using this method without super() and with super().

''' method added above'''


# PART 2.4: CUSTOMIZE: OVERRIDE THE CONSTRUCTOR
# Override the constructor in the Manager class. Make it so that Managers have
# an instance variable for department, describing which department they are
# over. Use super() to get access to all of the other instance variables

''' method added above '''
