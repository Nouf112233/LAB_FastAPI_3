from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine=create_engine("postgresql://postgres:Almasah1&2@localhost:5000/Schoole",echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)