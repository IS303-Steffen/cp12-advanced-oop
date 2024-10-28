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

class Employee: # class name is Employee
    companyName = "Python Co." # class variable

    def __init__(self, name, salary): # constructor
        self.name = name # instance variables
        self.salary = salary

    def give_raise(self, amount): # method
        if amount < 20_000:
            self.salary += amount
        else:
            self.salary += 20_000

    def display_status(self): # method
        return f"My name is {self.name} and I have a salary of {self.salary}"


emp_1 = Employee('John Doe', 50000) # creating new employee object
print(emp_1.display_status())
emp_1.give_raise(5000)
print(emp_1.display_status())



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

class Manager(Employee): # class called Manager is the sub class. The super class that Manager inherits from is Employee
    def __init__(self, name, salary, department):
        super().__init__(name, salary)  # Call the constructor of Employee
        self.department = department # instance variable that only applies to Managers, not employees.

    def give_raise(self, amount, bonus=0.1):  # Override the give_raise method to include a bonus
        # strategy 1: just write out new logic:
        # if amount < 20_000:
        #     self.salary += amount
        # else:
        #     self.salary += 20_000
        
        # strategy 2: use super()
        new_amount = amount + amount * bonus
        super().give_raise(new_amount)  # Call the original give_raise method with new amount

    # you can make any other methods you want. 
    def give_praise(self, otherEmployeeObject):
        return f"Wow {otherEmployeeObject.name}, you're doing awesome!!!"

manager_1 = Manager('Jane Smith', 60000, 'IT') # creating new manager object
print(manager_1.give_praise(emp_1))
print(manager_1.display_status()) # note how it has access to employee methods
manager_1.give_raise(5000)   # note that it calls the overridden give_raise method
print(manager_1.display_status())

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
