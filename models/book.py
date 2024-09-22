from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base, SessionLocal

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    publication_year = Column(Integer, nullable=False)

    author = relationship('Author')

    @classmethod
    def create(cls, title, author_id, publication_year):
        with SessionLocal() as db:
            try:
                book = cls(title=title, author_id=author_id, publication_year=publication_year)
                db.add(book)
                db.commit()
                db.refresh(book)
                return book
            except Exception as e:
                db.rollback()  # Rollback in case of error
                print(f"Error creating book: {e}")

    @classmethod
    def delete(cls, id):
        with SessionLocal() as db:
            try:
                book = db.query(cls).filter(cls.id == id).first()
                if book:
                    db.delete(book)
                    db.commit()
            except Exception as e:
                db.rollback()
                print(f"Error deleting book: {e}")

    @classmethod
    def get_all(cls):
        with SessionLocal() as db:
            try:
                books = db.query(cls).all()
                return books
            except Exception as e:
                print(f"Error retrieving books: {e}")
                return []

    @classmethod
    def find_by_id(cls, id):
        with SessionLocal() as db:
            try:
                book = db.query(cls).filter(cls.id == id).first()
                return book
            except Exception as e:
                print(f"Error finding book by ID: {e}")
                return None

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', author_id={self.author_id}, publication_year={self.publication_year})>"
