# ==============================================================================
# START OF CLEAN CLASS DEFINITIONS
# ==============================================================================

# --- Class 1: LibraryItem (Clean and Final Version for this exercise) ---
class LibraryItem:
    def __init__(self, title_of_item, publication_year):
        self.title = title_of_item
        self._publication_year = None
        self.set_publication_year(publication_year)
        self.__item_id = self._generate_internal_id()
        print(f"LibraryItem '{self.title}' (ID: {self.__item_id}) initialized.") # Modified print

    def _generate_internal_id(self):
        return f"ID-{hash(self.title[:5])}-{id(self)}"

    def get_publication_year(self):
        return self._publication_year

    def set_publication_year(self, new_year):
        try:
            year_as_int = int(new_year)
            if year_as_int < -4000 or year_as_int > 2050:
                print(f"Warning (Title: {self.title}): Publication year {year_as_int} unusual. Setting to 0.")
                self._publication_year = 0
            else:
                self._publication_year = year_as_int
        except ValueError:
            print(f"Error (Title: {self.title}): Invalid year format '{new_year}'. Setting to 0.")
            self._publication_year = 0

    def get_item_details(self):
        return f"Title: {self.title}, Year: {self.get_publication_year()}"

    def display_item_type(self):
        print("I am a generic LibraryItem.")

    def get_internal_id_display(self):
        return f"Internal System ID: {self.__item_id}"

# --- Class 2: Book (Clean and Final Version for this exercise) ---
class Book(LibraryItem):
    def __init__(self, title_of_item, publication_year, author_name, isbn_param):
        super().__init__(title_of_item, publication_year)
        self.author = author_name
        self._isbn_number = None
        self.set_isbn(isbn_param)
        print(f"Book '{self.title}' by {self.author} initialized.") # Added init print

    def get_item_details(self):
        basic_details = super().get_item_details()
        return f"{basic_details}, Author: {self.author}, ISBN: {self.get_isbn()}"

    def display_item_type(self):
        print("I am a Book.")

    def display_book_specific_details(self):
        print(f"Author: {self.author}, ISBN: {self.get_isbn()}")

    def get_isbn(self):
        return self._isbn_number

    def set_isbn(self, new_isbn_value):
        print(f"\nDEBUG: set_isbn called for '{self.title}' with new_isbn_value: '{new_isbn_value}' (type: {type(new_isbn_value)})")
        print(f"DEBUG: Current self._isbn_number before anything: '{self._isbn_number}'")

        # First, handle type error
        if not isinstance(new_isbn_value, str):
            print(f"Error (Book: {self.title}): ISBN must be a string. Got type {type(new_isbn_value)}. Current ISBN ('{self._isbn_number}') is NOT changed.")
            if self._isbn_number is None:
                self._isbn_number = "Invalid ISBN (Type Error)"
            return # <<< This return is important for the type error case

        # If it's a string, proceed with format validation
        simplified_isbn = new_isbn_value.replace("-", "")
        length_of_simplified = len(simplified_isbn)

        print(f"DEBUG: simplified_isbn: '{simplified_isbn}', length_of_simplified: {length_of_simplified}")

        if length_of_simplified == 10 or length_of_simplified == 13:
            print(f"DEBUG: Condition (length == 10 or length == 13) is TRUE for length {length_of_simplified}")
            old_isbn = self._isbn_number
            self._isbn_number = new_isbn_value
            print(f"Info (Book: {self.title}): ISBN changed from '{old_isbn}' to '{self._isbn_number}'.")
        else:
            print(f"DEBUG: Condition (length == 10 or length == 13) is FALSE for length {length_of_simplified}")
            print(f"Error (Book: {self.title}): Invalid ISBN format '{new_isbn_value}'. Length w/o hyphens: {length_of_simplified}. Current ISBN ('{self._isbn_number}') is NOT changed.")
            if self._isbn_number is None:
                self._isbn_number = "Invalid ISBN (Format Error)"
        
        print(f"DEBUG: self._isbn_number at end of set_isbn: '{self._isbn_number}'")
        # NO MORE CODE AFTER THIS LINE IN THIS METHOD # NO MORE CODE AFTER THIS LINE IN THIS METHOD # If it already had a value (valid or previously invalid), we don't change it here, just report the error.   
# --- Class 3: Magazine (Clean and minimal for now) ---
class Magazine(LibraryItem):
    def __init__(self, title_of_item, publication_year, issue_number, editor_name):
        super().__init__(title_of_item, publication_year)
        self.issue = issue_number
        self.editor = editor_name
        print(f"Magazine '{self.title}' initialized.") # Added init print

    def get_item_details(self):
        basic_details = super().get_item_details()
        return f"{basic_details}, Issue: {self.issue}, Editor: {self.editor}"
    


    def display_item_type(self):
        print("I am a Magazine.")

# --- Class 4: Dvd (Clean and minimal for now) ---
class Dvd(LibraryItem):
    def __init__(self, title_of_item, publication_year, director_name):
        super().__init__(title_of_item, publication_year)
        self.director_name = director_name
        print(f"DVD '{self.title}' initialized.") # Added init print

    def get_item_details(self):
        basic_details = super().get_item_details()
        return f"{basic_details}, Director: {self.director_name}"

    def display_item_type(self):
        print("I am a DVD.")

# --- Class 5: AudioBook (Clean and minimal for now) ---
class AudioBook(LibraryItem):
    def __init__(self, title_of_item, publication_year, narrator_name, duration_in_hours):
        super().__init__(title_of_item, publication_year)
        self.narrator_name = narrator_name
        self.duration_in_hours = duration_in_hours
        print(f"AudioBook '{self.title}' initialized.") # Added init print

    def get_item_details(self):
        basic_details = super().get_item_details()
        return f"{basic_details}, Narrator: {self.narrator_name}, Duration: {self.duration_in_hours}h"

    def display_item_type(self):
        print("I am an Audiobook.")

# ==============================================================================
# END OF CLEAN CLASS DEFINITIONS
# =================================G=============================================

# --- YOUR TEST SCRIPT (Keep this exactly as it was) ---
print("\n--- Creating Books ---")
book_valid_isbn = Book("The Pragmatic Programmer", 1999, "Andy Hunt & Dave Thomas", "978-0201616224")
print("-----")
book_invalid_isbn_short = Book("A Short Story", 2020, "Jane Doe", "12345")
print("-----")
book_invalid_isbn_long = Book("A Long Tale", 2021, "John Smith", "123456789012345")
print("-----")
book_no_hyphen_valid = Book("Structure and Interpretation", 1996, "Abelson & Sussman", "0262011530")
print("-----")
book_bad_type_isbn = Book("Another Book", 2022, "Test Author", 1234567890) # Non-string ISBN
print("-----")

print("\n--- Book Details (After Creation) ---")
print(f"1. {book_valid_isbn.get_item_details()}")
print(f"2. {book_invalid_isbn_short.get_item_details()}")
print(f"3. {book_invalid_isbn_long.get_item_details()}")
print(f"4. {book_no_hyphen_valid.get_item_details()}")
print(f"5. {book_bad_type_isbn.get_item_details()}")
print("-----")

print(f"\n--- Testing set_isbn on '{book_valid_isbn.title}' (current ISBN: {book_valid_isbn.get_isbn()}) ---")
test_string = "isbn-short"
simplified_test_string = test_string.replace("-", "")
print(f"LITERAL TEST: String is '{test_string}', Simplified is '{simplified_test_string}', Length of simplified is {len(simplified_test_string)}")
# The original line 191:
book_valid_isbn.set_isbn("isbn-short")



book_valid_isbn.set_isbn("123-456-7890") # Valid 10-digit
print(f"Details after setting valid 10-digit: {book_valid_isbn.get_item_details()}")
print("-----")

book_valid_isbn.set_isbn("this-is-too-long") # Invalid
print(f"Details after setting invalid format (should not change from previous valid): {book_valid_isbn.get_item_details()}")
print("-----")

book_valid_isbn.set_isbn(99999) # Invalid type
print(f"Details after setting invalid type (should not change from previous valid): {book_valid_isbn.get_item_details()}")
print("-----")

print(f"\n--- Testing set_isbn on '{book_invalid_isbn_short.title}' (current ISBN: {book_invalid_isbn_short.get_isbn()}) ---")
book_invalid_isbn_short.set_isbn("0987654321") # Now set a valid one
print(f"Details after setting valid ISBN: {book_invalid_isbn_short.get_item_details()}")
print("-----")

DEBUG: set_isbn called for 'The Pragmatic Programmer' with new_isbn_value: 'isbn-short' (type: <class 'str'>)
DEBUG: Current self._isbn_number before anything: '123-456-7890'
DEBUG: simplified_isbn: 'isbnshort', length_of_simplified: 9
DEBUG: Condition (length == 10 or length == 13) is FALSE for length 9
Error (Book: The Pragmatic Programmer): Invalid ISBN format 'isbn-short'. Length w/o hyphens: 9. Current ISBN ('123-456-7890') is NOT changed.
DEBUG: self._isbn_number at end of set_isbn: '123-456-7890'
Details after setting 'isbn-short' (should not change from previous valid): Title: The Pragmatic Programmer, Year: 1999, Author: Andy Hunt & Dave Thomas, ISBN: 123-456-7890