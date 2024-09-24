from models.base import SessionLocal
from models.book import Book
from models.author import Author
from models.edition import Edition

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
        book1 = Book.create("Book One", author1.id, 2021)
        book2 = Book.create("Book Two", author2.id, 2022)
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

        # Test adding editions
        print("\nAdding editions...")
        edition1 = Edition.create(book1.id, 1, "978-3-16-148410-0")
        edition2 = Edition.create(book2.id, 1, "978-3-16-148411-7")
        print(f"Added editions: {edition1}, {edition2}")

        # Test listing editions
        print("\nListing editions...")
        editions = Edition.get_all()
        for edition in editions:
            print(f"{edition.id}: Book ID: {edition.book_id}, Edition Number: {edition.edition_number}, ISBN: {edition.isbn}")

        # Test finding edition by ID
        print("\nFinding edition by ID...")
        found_edition = Edition.find_by_id(edition1.id)
        print(f"Found edition: Book ID: {found_edition.book_id}, Edition Number: {found_edition.edition_number}, ISBN: {found_edition.isbn}")

        # Test deleting editions, books, and authors
        print("\nDeleting editions, books, and authors...")
        Edition.delete(edition1.id)
        Book.delete(book1.id)
        Author.delete(author1.id)
        print(f"Deleted edition with ID {edition1.id}, book with ID {book1.id}, and author with ID {author1.id}")

        # Final listing to confirm deletions
        print("\nFinal listing of authors, books, and editions...")
        authors = Author.get_all()
        books = Book.get_all()
        editions = Edition.get_all()
        print(f"Authors: {authors}")
        print(f"Books: {books}")
        print(f"Editions: {editions}")

    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    test_database()
