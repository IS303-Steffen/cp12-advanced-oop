from helper_functions import clear_screen
clear_screen()

# ====================
# INHERITANCE PRACTICE
# ====================


# 1. PRACTICE:
# You are given this code for Books and LibraryMembers:

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

class LibraryMember:
    def __init__(self, name):
        self.name = name
        self.checked_out_books = []

    def check_out_book(self, book):

        limit = getattr(self, 'check_out_limit', 2)

        if len(self.checked_out_books) >= limit:
            print(f"{self.name} cannot check out more than {limit} books.")
        elif book.is_available is False:
            print(f"The book '{book.title}' is currently not available.")
        else:
            book.is_available = False
            self.checked_out_books.append(book)
            print(f"{self.name} has checked out '{book.title}'. They now have {len(self.checked_out_books)} book(s) checked out.")

    def return_book(self, book):
        if book in self.checked_out_books:
            book.is_available = True
            self.checked_out_books.remove(book)
            print(f"{self.name} has returned '{book.title}'. They now have {len(self.checked_out_books)} book(s) checked out.")
        else:
            print(f"{self.name} cannot return a book they haven't checked out.")

book_1 = Book("Pride and Prejudice", "Jane Austen")
book_2 = Book("Moby-Dick", "Herman Melville")
book_3 = Book("Great Expectations", "Charles Dickens")
book_4 = Book("War and Peace", "Leo Tolstoy")
book_5 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book_6 = Book("Crime and Punishment", "Fyodor Dostoevsky")
book_7 = Book("Jane Eyre", "Charlotte Brontë")
book_8 = Book("Wuthering Heights", "Emily Brontë")
book_9 = Book("The Odyssey", "Homer")
book_10 = Book("To Kill a Mockingbird", "Harper Lee")


# YOUR TASK:
# Create a new class PremiumLibraryMembers that inherits from LibraryMember
# class variabes:
#   starting_check_out_limit = 3
# instance variables:
#   - all those from LibraryMembers
#   - check_out_limit (should be equal to starting_check_out_limit)
#   - all_time_num_checked_out (should be 0 to start)
#
# Make it so that when PremiumLibraryMembers check out a book, it uses
# their check_out_limit instead of the default 2 that normal LibraryMembers
# have. It should also update the all_time_num_checked_out number each time
# they succesfully check out a book.
# Create a PremiumLibraryMember and show that they can check out
# 3 books instead of just 2.

# BONUS IMPROVEMENTS
# 1. Can you figure out a way to write check_out_book so that you dont repeat
#    nearly all the code from LibraryMember in PremiumLibraryMember? Some ideas
#    would be using super(), probably with either an extra parameter, or using
#    a function like getattr() (look it up!)
#
# 2. Add a method to PremiumLibraryMember called calculate_check_out_limit that
#    increases the check_out_limit by one each time a PremiumLibraryMember
#    checks out 4 books (so if they have checked out 4 their limit should be 4,
#    if they've checked out 8 their limit should be 5, if they've checked out
#    12 their limit should be 6, etc.) You might find floor division // useful.

class PremiumLibraryMember(LibraryMember):
    starting_check_out_limit = 3
    def __init__(self, name):
        super().__init__(name)
        self.check_out_limit = PremiumLibraryMember.starting_check_out_limit
        self.all_time_num_checked_out = 0

    def check_out_book(self, book):
        initial_book_count = len(self.checked_out_books) # to see if all time increased
        super().check_out_book(book)

        if len(self.checked_out_books) > initial_book_count: # if their length is higher, increase all time count
            self.all_time_num_checked_out += 1

        self.calculate_check_out_limit() # calculate a new check out limit if it increased.

    def calculate_check_out_limit(self):
        increase_amount = self.all_time_num_checked_out // 4
        self.check_out_limit = PremiumLibraryMember.starting_check_out_limit + increase_amount


james_member = LibraryMember("James")
anna_prem_member = PremiumLibraryMember("Anna")

# Regular member checking out books
james_member.check_out_book(book_1)
james_member.check_out_book(book_2)
james_member.check_out_book(book_3)
james_member.check_out_book(book_4)  # Should not be allowed

# Premium member checking out books
anna_prem_member.check_out_book(book_4)
anna_prem_member.check_out_book(book_5)
anna_prem_member.check_out_book(book_6)
anna_prem_member.check_out_book(book_7)  # won't work
anna_prem_member.return_book(book_6)
anna_prem_member.check_out_book(book_7)  # now can work
anna_prem_member.check_out_book(book_8) # limit has increased

