# from sqlmodel import SQLModel, Field,Column
# import sqlalchemy.dialects.postgresql as pg
# from uuid import UUID, uuid4
# from datetime import datetime


from sqlalchemy import Column, String, Text, DateTime, Table
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4
from datetime import datetime

Base = declarative_base()

class Books(Base):
    """
    This class represents a book in the database
    """
    __tablename__ = 'books'

    uid = Column(PGUUID, primary_key=True, unique=True, default=uuid4)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    isbn = Column(String, unique=True, nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self) -> str:
        return f"Book => {self.title}"