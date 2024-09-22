from sqlalchemy import Column, Integer, String
from models.base import Base, SessionLocal

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    country = Column(String, nullable=False)

    @classmethod
    def create(cls, name, country):
        db = SessionLocal()
        try:
            author = cls(name=name, country=country)
            db.add(author)
            db.commit()
            db.refresh(author)
            return author
        except Exception as e:
            db.rollback()  # Rollback in case of error
            print(f"Error creating author: {e}")
        finally:
            db.close()

    @classmethod
    def delete(cls, id):
        db = SessionLocal()
        try:
            author = db.query(cls).filter(cls.id == id).first()
            if author:
                db.delete(author)
                db.commit()
        except Exception as e:
            db.rollback()
            print(f"Error deleting author: {e}")
        finally:
            db.close()

    @classmethod
    def get_all(cls):
        db = SessionLocal()
        try:
            authors = db.query(cls).all()
            return authors
        except Exception as e:
            print(f"Error retrieving authors: {e}")
            return []
        finally:
            db.close()

    @classmethod
    def find_by_id(cls, id):
        db = SessionLocal()
        try:
            author = db.query(cls).filter(cls.id == id).first()
            return author
        except Exception as e:
            print(f"Error finding author by ID: {e}")
            return None
        finally:
            db.close()

    def __repr__(self):
        return f"<Author(id={self.id}, name='{self.name}', country='{self.country}')>"
