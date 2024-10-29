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

# ====================
# MULTIPLE INHERITANCE
# ====================

'''
OVERVIEW
--------
Multiple inheritance is when you have more than 1 super/parent class.

We won't use it on any assignment (hence it is marked as extra) but it could
potentially be very useful in certain situations. The order of inheritance
goes from left to right, and it also grabs and parent classes of the parent
classes, as many down the chain as you specify.
'''

class Employee:
        def __init__(self):
            self.first_name = ""
            self.last_name = ""
            print("Employee Constuctor")

        def my_print(self) :
            print("Employee my_print()")

class Checker(Employee):
    def __init__(self):
        super().__init__()
        self.til_number = 0
        self.balanced_til = True
        print("Checker Constuctor")        

    def my_print(self):
        super().my_print()
        print("Checker my_print()")

class Stocker(Employee):
    def __init__(self):
        super().__init__()
        self.can_lift_50lbs = False
        print("Stocker Constuctor")

    def my_print(self):
        super().my_print()
        print("Stocker my_print()")

class GroceryEmployee(Checker, Stocker): # Notice here we reference 2 classes
    def __init__ (self):
        super().__init__() 
        print("Grocery_Employee Constuctor")        

'''
Note that super() can sometimes be confusing.
Feel free to call the specific class instead.
class GroceryEmployee(Checker, Stocker) :
    def __init__ (self):
        Checker.__init__(self)
        Stocker.__init__(self)
        Employee.__init__(self)
        print("Grocery_Employee Constuctor")

'''   


        
employee = GroceryEmployee()
print(GroceryEmployee.mro()) # method resolution order
print("\n\n")
employee.my_print()




 