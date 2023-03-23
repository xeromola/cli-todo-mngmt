from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from database import SqlAlchemyService

# Create a declarative base for defining ORM models
Base = declarative_base()


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    task = Column(String, nullable=False)


# Creates the table in sqlite
alchemy = SqlAlchemyService()
Base.metadata.create_all(alchemy.engine)
