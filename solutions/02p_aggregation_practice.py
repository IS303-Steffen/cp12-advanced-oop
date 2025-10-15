from helper_functions import clear_screen
clear_screen()

# ======================
# AGGREGATION - PRACTICE
# ======================

# 1. PRACTICE
# Create a simplified system to model the relationship between students and
# class sections, showcasing aggregation.
# Define two classes:
#   ClassSection: with attributes for section_id and course_name,
#   Student: with attributes for name and enrolled_sections, the latter being
#            a list to track the class sections a student is enrolled in.
# Students can be directly enrolled in sections by adding ClassSection
# instances to their enrolled_sections list.

# Code a way for any Student object to display their enrolled class sections.
# Make objects of each class, add ClassSections to student objects,
# and diplay which students are in which class.


class ClassSection:
    def __init__(self, section_id, course_name):
        self.section_id = section_id
        self.course_name = course_name

class Student:
    def __init__(self, name):
        self.name = name
        self.enrolled_sections = []

    def print_enrolled_sections(self):

        message = f"{self.name} is enrolled in the following sections:"
        for section in self.enrolled_sections:
            message += f"\n\t{section.section_id} {section.course_name}"
        return message

# Example setup
section_1 = ClassSection("CS101", "Introduction to Programming")
section_2 = ClassSection("MA101", "Calculus I")
section_3 = ClassSection("EN101", "English Literature")

student_1 = Student("Alex")
student_1.enrolled_sections.extend([section_1, section_2])

student_2 = Student("Jordan")
student_2.enrolled_sections.extend([section_2, section_3])

# Display enrolled sections
print(student_1.print_enrolled_sections())
print(student_2.print_enrolled_sections())
