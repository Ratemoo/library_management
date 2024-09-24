from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///library.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def create_tables():
    Base.metadata.create_all(bind=engine)

# Remove the import of Edition here

if __name__ == "__main__":
    create_tables()
