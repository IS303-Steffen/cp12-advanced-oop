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

# =========================
# PRIVATE & PROTECTED SCOPE
# =========================

'''
OVERVIEW
--------
Scope refers to where you can access a variable. We've already learned about:

- Global Scope:
    Variables declared outside any function or class, accessible throughout the
    module.

- Local Scope:
    Variables created within a function, accessible only within that function.

In classes, there are additional types of access control:

- Public Scope:
    Class/instance variables or methods are accessible outside the class
    through an object instance.

- Protected Scope (Python convention):
    Class/instance variables or methods prefixed with a single underscore `_`
    are intended to be accessible only within the class and subclasses.

- Private Scope (Python's approach):
    Class/instance variables or methods prefixed with double underscores `__`
    are “name-mangled” to reduce accidental access, making them accessible
    only within the class.

SYNTAX
------
TYPE:       SYNTAX:     (INTENDED) PURPOSE:             
public      var_name     access class/instance
                         variables anywhere
                            
protected   _var_name    confine access to variables
                         to just the class and subclasses

private     __var_name   confine access to variables
                         to just the class
'''

class Account: # name of the class is Account
    total_money = 0 # this is a class variable

    def __init__(self, account_holder, balance = 0):
        self._account_holder = account_holder # these are the instance variables
        self.__balance = balance

        Account.total_money = Account.total_money + balance # this updates the class variable

    def deposit_or_withdraw(self, amount):
        self.__balance = self.__balance + amount

        Account.total_money = Account.total_money + amount

    def display_balance(self):
        print(f"Account holder: {self._account_holder} has a current balance of: {self.__balance}")

scrooge = Account("Scrooge McDuck", 100_000_000)

# 1.1 DIRECTLY CHANGE A VARIABLE
# Using the provided Account object below, try to directly change Scrooge's
# balance variable without using deposit_or_withdraw. Are there
# logical problems with doing this?

# scrooge.balance = 0

# 1.2 MAKING A VARIABLE PRIVATE
# Add two underscores to the beginning of the `balance` variable in the Account
# class. Now try to change the `__balance` variable through the `scrooge`
# object. What happens?
# Try setting a break point and hover over the `scrooge` variable and see
# what happened to the `__balance` variable when you made it private.
# Now change the value through deposit_or_withdraw.

# scrooge.__balance = 0 # doesn't work

scrooge.deposit_or_withdraw(10_000)

'''
WHY MAKE SOMETHING PRIVATE?
---------------------------
Often, you have logic that needs to be followed when you are changing a value,
like this case where you want to update the total_money class variable.

By preventing direct access to a variable, you make sure that it can only
be interacted with by calling methods (or not interacted with at all) so that
that variable doesn't get changed somewhere else in the code when it shouldn't
be changed.
'''

# 2. MAKE A (SORT OF) PROTECTED VARIABLE
# Change `account_holder` to have a single underscore at the start
# Then try printing it through the `scrooge` object.
print(scrooge._account_holder)

'''
WHAT IS THE POINT OF PROTECTED VARIABLES?
-----------------------------------------
In other programming languages, if you make a variable protected, you literally
cannot access it outside of the class/sub classes. In python however, there is
no such thing as protected variables. Using an underscore `_` just signifies
to anyone reading your code "this is intended to be a private variable that 
you don't mess with. Don't touch it unless you really know what you're doing"
but there isn't anything actually stopping them from getting to it.

'''
