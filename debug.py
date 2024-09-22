from models.base import SessionLocal
from models.book import Book
from models.author import Author

def test_database():
    session = SessionLocal()

    try:
        # Test adding authors
        print("\nAdding authors...")
        author1 = Author.create("Author One", "Kenya")
        author2 = Author.create("Author Two", "USA")
        print(f"Added authors: {author1.name}, {author2.name}")

        # Test listing authors
        print("\nListing authors...")
        authors = Author.get_all()
        for author in authors:
            print(f"{author.id}: {author.name}, {author.country}")

        # Test finding author by ID
        print("\nFinding author by ID...")
        found_author = Author.find_by_id(author1.id)
        print(f"Found author: {found_author.name}, {found_author.country}")

        # Test adding books
        print("\nAdding books...")
        book1 = Book.create("Book One", author1.id, 2021)  # Added publication_year
        book2 = Book.create("Book Two", author2.id, 2022)  # Added publication_year
        print(f"Added books: {book1.title}, {book2.title}")

        # Test listing books
        print("\nListing books...")
        books = Book.get_all()
        for book in books:
            print(f"{book.id}: {book.title}, Author ID: {book.author_id}, Year: {book.publication_year}")

        # Test finding book by ID
        print("\nFinding book by ID...")
        found_book = Book.find_by_id(book1.id)
        print(f"Found book: {found_book.title}, Author ID: {found_book.author_id}, Year: {found_book.publication_year}")

        # Test deleting books and authors
        print("\nDeleting books and authors...")
        Book.delete(book1.id)
        Author.delete(author1.id)
        print(f"Deleted book with ID {book1.id} and author with ID {author1.id}")

        # Final listing to confirm deletions
        print("\nFinal listing of authors and books...")
        authors = Author.get_all()
        books = Book.get_all()
        print(f"Authors: {authors}")
        print(f"Books: {books}")

    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    test_database()
