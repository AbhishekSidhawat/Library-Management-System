import sys
from database import DBconnect

class BookInfo:
    def __init__(self):
        # Initialize the DB connection and display the menu
        self.db = DBconnect()
        self.menu()

    def menu(self):
        # Display the menu options for the user
        user_input = '''
        1. Add book
        2. View all books
        3. Delete a book
        4. Exit
        '''
        print(user_input)
        self.user_choice()

    def user_choice(self):
        # Handle the user's choice for the operation
        while True:
            try:
                # Prompt the user to input a choice
                choice = int(input("\nEnter the operation (1-4):- "))
                if choice == 1:
                    self.add()  # Call the add function if choice is 1
                elif choice == 2:
                    self.view()  # Call the view function if choice is 2
                elif choice == 3:
                    self.delete()  # Call the delete function if choice is 3
                elif choice == 4:
                    print("Thank you for using the program. Goodbye!")  # Exit message
                    break  # Break the loop to exit the program
                else:
                    print("Please enter a valid input.")  # Invalid input message
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")  # Handle invalid input

    def add(self):
        # Handle adding a new book to the database
        try:
            # Prompt the user for book details
            title = input("Enter the book title: ")
            author = input("Enter the author name: ")
            copies_available = int(input("Enter the number of copies: "))
            # Add the book to the database using the DBconnect class
            response = self.db.add(title, author, copies_available)
            if response == 1:
                print("Book added successfully.")  # Success message
            else:
                print("Failed to add the book.")  # Failure message
        except ValueError:
            print("Invalid input. Please enter the correct data types.")  # Handle invalid data input
        self.menu()  # Return to the menu after the operation

    def view(self):
        # This function will be implemented later for viewing all books
        pass

    def delete(self):
        # This function will be implemented later for deleting a book
        pass

# Main program execution
if __name__ == "__main__":
    BookInfo()  # Create an instance of the BookInfo class to run the program
