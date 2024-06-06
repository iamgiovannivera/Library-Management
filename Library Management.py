# 1. Setting Up the MySQL Database


# pip install mysql-connector-python



# CREATE DATABASE library_management;

# USE library_management;

# CREATE TABLE authors (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255) NOT NULL,
#     biography TEXT
# );

# CREATE TABLE genres (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255) NOT NULL,
#     description TEXT,
#     category VARCHAR(50)
# );

# CREATE TABLE books (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     title VARCHAR(255) NOT NULL,
#     author_id INT,
#     genre_id INT,
#     isbn VARCHAR(13) NOT NULL,
#     publication_date DATE,
#     availability BOOLEAN DEFAULT 1,
#     FOREIGN KEY (author_id) REFERENCES authors(id),
#     FOREIGN KEY (genre_id) REFERENCES genres(id)
# );

# CREATE TABLE users (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255) NOT NULL,
#     library_id VARCHAR(10) NOT NULL UNIQUE
# );

# CREATE TABLE borrowed_books (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     user_id INT,
#     book_id INT,
#     borrow_date DATE NOT NULL,
#     return_date DATE,
#     FOREIGN KEY (user_id) REFERENCES users(id),
#     FOREIGN KEY (book_id) REFERENCES books(id)
# );


# 2. Establishing Database Connection




# import mysql.connector

# def get_db_connection():
#     connection = mysql.connector.connect(
#         host="localhost",
#         user="your_username",
#         password="your_password",
#         database="library_management"
#     )
#     return connection



# 3. Extending OOP Classes



# class Book:
#     def __init__(self, id, title, author_id, genre_id, isbn, publication_date, availability=True):
#         self.id = id
#         self.title = title
#         self.author_id = author_id
#         self.genre_id = genre_id
#         self.isbn = isbn
#         self.publication_date = publication_date
#         self.availability = availability

#     @staticmethod
#     def add_book(connection, title, author_id, genre_id, isbn, publication_date):
#         cursor = connection.cursor()
#         cursor.execute(
#             "INSERT INTO books (title, author_id, genre_id, isbn, publication_date, availability) VALUES (%s, %s, %s, %s, %s, %s)",
#             (title, author_id, genre_id, isbn, publication_date, True)
#         )
#         connection.commit()
        
        
        
# 4. Implementing Menu Actions




# def add_new_book():
#     title = input("Enter book title: ")
#     author_id = int(input("Enter author ID: "))
#     genre_id = int(input("Enter genre ID: "))
#     isbn = input("Enter ISBN: ")
#     publication_date = input("Enter publication date (YYYY-MM-DD): ")

#     connection = get_db_connection()
#     Book.add_book(connection, title, author_id, genre_id, isbn, publication_date)
#     connection.close()
#     print("Book added successfully.")

# def display_all_books():
#     connection = get_db_connection()
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM books")
#     for (id, title, author_id, genre_id, isbn, publication_date, availability) in cursor:
#         print(f"{id}: {title} by {author_id}, Genre: {genre_id}, ISBN: {isbn}, Published: {publication_date}, Available: {availability}")
#     connection.close()
    
    
    
    
# 5. Creating the Command-Line Interface (CLI)




# def main_menu():
#     while True:
#         print("\nMain Menu:")
#         print("1. Book Operations")
#         print("2. User Operations")
#         print("3. Author Operations")
#         print("4. Genre Operations")
#         print("5. Quit")

#         choice = input("Enter your choice: ")

#         if choice == '1':
#             book_operations()
#         elif choice == '2':
#             user_operations()
#         elif choice == '3':
#             author_operations()
#         elif choice == '4':
#             genre_operations()
#         elif choice == '5':
#             break
#         else:
#             print("Invalid choice. Please try again.")

# def book_operations():
#     while True:
#         print("\nBook Operations:")
#         print("1. Add a new book")
#         print("2. Borrow a book")
#         print("3. Return a book")
#         print("4. Search for a book")
#         print("5. Display all books")
#         print("6. Back to Main Menu")

#         choice = input("Enter your choice: ")

#         if choice == '1':
#             add_new_book()
#         elif choice == '2':
#             borrow_book()
#         elif choice == '3':
#             return_book()
#         elif choice == '4':
#             search_book()
#         elif choice == '5':
#             display_all_books()
#         elif choice == '6':
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main_menu()