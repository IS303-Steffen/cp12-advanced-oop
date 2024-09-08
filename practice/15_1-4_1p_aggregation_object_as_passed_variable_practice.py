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

# Aggregation Practice Problem

'''
Create a simplified system to model the relationship between students and class sections, showcasing aggregation.
Define two classes:
    ClassSection, with attributes for section_id and course_name,
    Student, with attributes for name and enrolled_sections, the latter being a list to track the class sections a student is enrolled in.
Students can be directly enrolled in sections by adding ClassSection instances to their enrolled_sections list.

Code a way for any Student object to display their enrolled class sections.
Make objects of each class, add ClassSections to student objects, and diplay which students are in which class.
'''

