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
        except:
            # Exit the program if the connection fails
            sys.exit("Failed to connect to the database.")

    def add(self, title, author, copies_available):
        # This method will add a new book to the database
        try:
            # SQL query to insert a new book into the books table
            sql = "INSERT INTO books (title, author, copies_available) VALUES (%s, %s, %s)"
            values = (title, author, copies_available)  # Values to be inserted
            self.cursor.execute(sql, values)  # Execute the query with the provided values
            self.conn.commit()  # Commit the transaction to the database
        except:
            # Return -1 if there's an error during the insertion
            return -1
        else:
            # Return 1 if the book is added successfully
            return 1

    def view(self):
        try: 
            sql = "SELECT * FROM books"  # Assuming 'books' table is inside 'library' database
            self.cursor.execute(sql)
            return self.cursor.fetchall() 
        except:
            print(f"No book available")
            return [] 

    def delete(self):
        # This method will be implemented later to delete a book from the database
        pass
