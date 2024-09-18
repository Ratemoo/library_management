import sys
from models.author import Author
from models.book import Book

def main():
    while True:
        print("\nLibrary Management System CLI")
        print("1. Create Author")
        print("2. Delete Author")
        print("3. Display All Authors")
        print("4. Find Author by ID")
        print("5. Create Book")
        print("6. Delete Book")
        print("7. Display All Books")
        print("8. Find Book by ID")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter author's name: ")
            country = input("Enter author's country: ")
            author = Author.create(name, country)
            print(f"Author created with ID {author.id}")

        elif choice == "2":
            id = int(input("Enter author ID to delete: "))
            Author.delete(id)
            print("Author deleted")

        elif choice == "3":
            authors = Author.get_all()
            for author in authors:
                print(f"ID: {author.id}, Name: {author.name}, Country: {author.country}")

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
            print(f"Book created with ID {book.id}")

        elif choice == "6":
            id = int(input("Enter book ID to delete: "))
            Book.delete(id)
            print("Book deleted")

        elif choice == "7":
            books = Book.get_all()
            for book in books:
                print(f"ID: {book.id}, Title: {book.title}, Author ID: {book.author_id}, Publication Year: {book.publication_year}")
        
        elif choice == "8":
            id = int(input("Enter book ID to find: "))
            book = Book.find_by_id(id)
            if book:
                print(f"ID: {book.id}, Title: {book.title}, Author ID: {book.author_id}, Publication Year: {book.publication_year}")
            else:
                print("Book not found")

        elif choice == "9":
            print("Exiting...")
            sys.exit()

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()