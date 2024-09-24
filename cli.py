import sys
from models.author import Author
from models.book import Book
from models.edition import Edition  # Import Edition
from models.base import create_tables

def main():
    authors_list = []
    books_list = []
    editions_list = []  # Initialize editions_list

    while True:
        print("\nLibrary Management System CLI")
        menu_options = [
            "1. Create Author",
            "2. Delete Author",
            "3. Display All Authors",
            "4. Find Author by ID",
            "5. Create Book",
            "6. Delete Book",
            "7. Display All Books",
            "8. Find Book by ID",
            "9. Create Edition",  # Add option for creating editions
            "10. Delete Edition",  # Add option for deleting editions
            "11. Display All Editions",  # Add option for displaying editions
            "12. Find Edition by ID",  # Add option for finding editions
            "13. Exit"
        ]
        print("\n".join(menu_options))
    
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter author's name: ")
            country = input("Enter author's country: ")
            author = Author.create(name, country)
            if author:
                authors_list.append((author.id, author.name, author.country))
                print(f"Author created with ID {author.id}")

        elif choice == "2":
            id = int(input("Enter author ID to delete: "))
            Author.delete(id)
            authors_list = [a for a in authors_list if a[0] != id]
            print("Author deleted")

        elif choice == "3":
            for author in authors_list:
                print(f"ID: {author[0]}, Name: {author[1]}, Country: {author[2]}")

        elif choice == "4":
            id = int(input("Enter author ID to find: "))
            author = Author.find_by_id(id)
            if author:
                print(f"ID: {author.id}, Name: {author.name}, Country: {author.country}")
            else:
                print("Author not found")

        elif choice == "5":
            title = input("Enter book title: ")
            author_id = int(input("Enter author ID: "))
            publication_year = int(input("Enter publication year: "))
            book = Book.create(title, author_id, publication_year)
            if book:
                books_list.append((book.id, book.title, book.author_id, book.publication_year))
                print(f"Book created with ID {book.id}")

        elif choice == "6":
            id = int(input("Enter book ID to delete: "))
            Book.delete(id)
            books_list = [b for b in books_list if b[0] != id]
            print("Book deleted")

        elif choice == "7":
            print("\nAll Books:")
            for book in books_list:
                print(f"ID: {book[0]}, Title: {book[1]}, Author ID: {book[2]}, Publication Year: {book[3]}")
        
        elif choice == "8":
            id = int(input("Enter book ID to find: "))
            book = Book.find_by_id(id)
            if book:
                print(f"ID: {book.id}, Title: {book.title}, Author ID: {book.author_id}, Publication Year: {book.publication_year}")
            else:
                print("Book not found")

        elif choice == "9":  # Create Edition
            book_id = int(input("Enter book ID: "))
            edition_number = int(input("Enter edition number: "))
            isbn = input("Enter ISBN: ")
            edition = Edition.create(book_id, edition_number, isbn)
            if edition:
                editions_list.append((edition.id, edition.book_id, edition.edition_number, edition.isbn))
                print(f"Edition created with ID {edition.id}")

        elif choice == "10":  # Delete Edition
            id = int(input("Enter edition ID to delete: "))
            Edition.delete(id)
            editions_list = [e for e in editions_list if e[0] != id]
            print("Edition deleted")

        elif choice == "11":  # Display All Editions
            print("\nAll Editions:")
            for edition in editions_list:
                print(f"ID: {edition[0]}, Book ID: {edition[1]}, Edition Number: {edition[2]}, ISBN: {edition[3]}")

        elif choice == "12":  # Find Edition by ID
            id = int(input("Enter edition ID to find: "))
            edition = Edition.find_by_id(id)
            if edition:
                print(f"ID: {edition.id}, Book ID: {edition.book_id}, Edition Number: {edition.edition_number}, ISBN: {edition.isbn}")
            else:
                print("Edition not found")

        elif choice == "13":  # Exit
            print("Exiting...")
            sys.exit()

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    create_tables()
    main()
