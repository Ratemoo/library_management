from sqlalchelmy import Column, Integer, String
from models.base import Base, SessionLocal

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    country = Column(String, nullable=False)

    @classmethod
    def create(cls, name, country):
        db=SessionLocal()
        author = cls(name=name, country=country)
        db.add(author)
        db.commit()
        db.refresh(author)
        db.close()
        return author

    @classmethod
    def delete(cls, id):
        db = SessionLocal()
        author = db.query(cls).filter(cls.id == id).first()
        if author:
            db.delete(author)
            db.commit()
        db.close()

    @classmethod
    def get_all(cls):
        db = SessionLocal()
        authors = db.query(cls).all()
        db.close()
        return authors

    @classmethod
    def find_by_id(cls, id):
        db = SessionLocal()
        author = db.query(cls).filter(cls.id == id).first()
        db.close()
        return author