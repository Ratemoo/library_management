from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base, SessionLocal

class Edition(Base):
    __tablename__ = 'editions'

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    edition_number = Column(Integer, nullable=False)
    isbn = Column(String, nullable=False)

    book = relationship('Book')

    @classmethod
    def create(cls, book_id, edition_number, isbn):
        db = SessionLocal()
        try:
            edition = cls(book_id=book_id, edition_number=edition_number, isbn=isbn)
            db.add(edition)
            db.commit()
            db.refresh(edition)
            return edition
        except Exception as e:
            db.rollback()  # Rollback in case of error
            print(f"Error creating edition: {e}")
        finally:
            db.close()

    @classmethod
    def get_all(cls):
        db = SessionLocal()
        try:
            editions = db.query(cls).all()
            return editions
        except Exception as e:
            print(f"Error retrieving editions: {e}")
            return []
        finally:
            db.close()

    @classmethod
    def find_by_id(cls, id):
        db = SessionLocal()
        try:
            edition = db.query(cls).filter(cls.id == id).first()
            return edition
        except Exception as e:
            print(f"Error finding edition by ID: {e}")
            return None
        finally:
            db.close()

    @classmethod
    def delete(cls, edition_id):
        db = SessionLocal()
        try:
            edition = db.query(cls).filter(cls.id == edition_id).first()
            if edition:
                db.delete(edition)
                db.commit()
                print(f"Deleted edition with ID {edition_id}")
            else:
                print(f"No edition found with ID {edition_id}")
        except Exception as e:
            print(f"Error deleting edition: {e}")
            db.rollback()
        finally:
            db.close()

    def __repr__(self):
        return f"<Edition(id={self.id}, book_id={self.book_id}, edition_number={self.edition_number}, isbn='{self.isbn}')>"
