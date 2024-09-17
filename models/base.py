from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchelmy.orm import sessionmaker

DATABASE_URL = "sqlite:///library.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()