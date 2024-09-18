from sqlalchelmy import Column, Integer, String, ForeignKey
from sqlalchelmy.orm import Relationship
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
        db = SessionLocal()
        book = cls(title=title, author_id=author_id, publication_year=publication_year)
        db.add(book)
        db.commit()
        db.refresh(book)
        db.close()
        return book

    @classmethod
    def delete(cls, id):
        db = SessionLocal()
        book = db.query(cls).filter(cls.id == id).first()
        if book:
            db.delete(book)
            db.commit()
        db.close()

    @classmethod
    def get_all(cls):
        db = SessionLocal()
        books = db.query(cls).all()
        db.close()
        return books

    @classmethod
    def find_by_id(cls, id):
        db = SessionLocal()
        book = db.query(cls).filter(cls.id == id).first()
        db.close()
        return book