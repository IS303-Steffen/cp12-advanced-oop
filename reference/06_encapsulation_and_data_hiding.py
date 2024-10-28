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

##### NEW NOTE####
# add the example of the library book here and how the list of books should be
# private so that the logic of adding and returnig books is preserved.


# Data Hiding

# Note, this is quite important in other languages
# In python, it is more like a light suggestion.
# Be aware of this, but for this class just stick with public
# unless very specifically told otherwise.

'''
    TYPE:       SYNTAX:     (INTENDED) PURPOSE:             
    public      varname     access class/instance
                            variables anywhere
                                
    protected   _varname    confine access to variables
                            to just the class and subclasses

    private     __varname   confine access to variables
                            to just the class
    

                            
'''



class Student :

    def __init__ (self) :
        self.birth_year = "2000"    # this is a PUBLIC variable accessible anywhere
        self._birth_city = "Provo"  # this is a PROTECTED variable
                                    # technicaly still availalbe anywhere, but the _ means the 
                                    # developer doesn't intend you to access it outside the class

                                    # in other languages (C#, Java, etc.) Protected means you can only
                                    # access these variables inside the class and any child classes


        self.__first_name = "John"  # this is a PRIVATE variable, hard to access outside the class
        self.__last_name = "Doe"    # the point is to not give access to variables that other users of the class don't need
                                    # e.g. simplify it for people that don't look at the source code.
                                    # techinically still accessible in python, but weirder to do.

        self.full_name = self.__last_name + ", " + self.__first_name

    def set_first_name(self, sFirst) :
        if isinstance(sFirst, str):
            self.__first_name = sFirst

    def get_first_name(self) :
        return (self.__first_name)
    

oStudent = Student()


# public variables are accessible very easily:
print(oStudent.birth_year)

# protected variables are also easily accessed,
# just know that if you see an underscore before a variable name, the developer probably wants you 
# to be cautious about accessing this:
print(oStudent._birth_city)

# private variables are harder:
#print(oStudent.__first_name) # this won't work

# private variables are still accessible, but 
# python will "mangle" the variable name so you aren't accidentally
# accessing it
print(oStudent._Student__first_name)


# The idea is that in OOP, the class developer is careful about letting
# other developers using the class directly access the variables
# that way, bugs are prevented, but it can also just simplify
# things for other developers that are using the code you created.

# for example, you could still get access to private variables through methods like this:
print(oStudent.get_first_name())

# and you can have more control over how variables are set using methods like this:
oStudent.set_first_name("Jimmy")

print(oStudent.get_first_name())