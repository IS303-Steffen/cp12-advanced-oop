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

# Multiple Inheritance (a class has more than 1 super/parent class)

# Not used as often. Be aware of it, but we won't spend time practicing.



class Employee :
        def __init__ (self) :
            self.first_name = ""
            self.last_name = ""
            print("Employee Constuctor")

        def my_print(self) :
            print("Employee my_print()")

class Checker(Employee) :
    def __init__ (self) :
        super().__init__()
        self.til_number = 0
        self.balanced_til = True
        print("Checker Constuctor")        

    def my_print(self) :
        super().my_print()
        print("Checker my_print()")

class Stocker(Employee) :
    def __init__ (self) :
        super().__init__ ()
        self.can_lift_50lbs = False
        print("Stocker Constuctor")

    def my_print(self) :
        super().my_print()
        print("Stocker my_print()")

class Grocery_Employee(Checker, Stocker) :
    def __init__ (self) :
        super().__init__() 
        print("Grocery_Employee Constuctor")        

#Note that super() can sometimes be confusing.
# Feel free to call the specific class instead.
# class Grocery_Employee(Checker, Stocker) :
#     def __init__ (self) :
#         Checker.__init__(self)
#         Stocker.__init__(self)
#         Employee.__init__(self)
#         print("Grocery_Employee Constuctor")     


        
oEmp = Grocery_Employee()
print(Grocery_Employee.mro()) # method resolution order
print("\n\n")
oEmp.my_print()




 