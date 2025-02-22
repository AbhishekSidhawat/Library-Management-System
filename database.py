import mysql.connector
import sys

class DBconnect:
    def __init__(self):
        # Initialize the connection to the MySQL database
        try:
            # Establish the connection using MySQL connector
            self.conn = mysql.connector.connect(
                host="localhost",  # Host where the database is located (local in this case)
                user="root",  # Database username
                password="1234",  # Database password
                database="library"  # Database name
            )
            self.cursor = self.conn.cursor()  # Create a cursor object to interact with the database
            print("Connected to Database Successfully!")  # Confirmation message upon successful connection
        except mysql.connector.Error as e:
            # Exit the program if the connection fails
            sys.exit(f"Failed to connect to the database: {e}")

    def add(self, title, author, copies_available):
        # This method will add a new book to the database
        try:
            # SQL query to insert a new book into the books table
            sql = "INSERT INTO books (title, author, copies_available) VALUES (%s, %s, %s)"
            values = (title, author, copies_available)  # Values to be inserted
            self.cursor.execute(sql, values)  # Execute the query with the provided values
            self.conn.commit()  # Commit the transaction to the database
            return 1  # Return 1 if the book is added successfully
        except mysql.connector.Error as e:
            # Print the error and return -1 if there's an error during the insertion
            print(f"Error adding book: {e}")
            return -1

    def view(self):
        try:
            sql = "SELECT * FROM books"  # Assuming 'books' table is inside 'library' database
            self.cursor.execute(sql)
            return self.cursor.fetchall()  # Return all books
        except mysql.connector.Error as e:
            # Handle error while fetching books
            print(f"Error fetching books: {e}")
            return []

    def delete(self, title):
        # Delete a book based on its title
        try:
            # Corrected SQL query using parameterized query format
            sql = "DELETE FROM books WHERE title = %s"  # Using parameterized query for safety
            values = (title,)  # Pass title as a tuple
            self.cursor.execute(sql, values)  # Execute the query with the provided title
            self.conn.commit()  # Commit the transaction
            if self.cursor.rowcount > 0:  # Check if any rows were deleted
                return 1  # Return 1 if a book was deleted
            else:
                return 0  # Return 0 if no book was found with the given title
        except mysql.connector.Error as e:
            # Print error and return -1 if there's an error during deletion
            print(f"Error deleting book: {e}")
            return -1
