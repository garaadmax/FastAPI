from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime
from auth.models import Users

Base = declarative_base()


class Books(Base):
    """
    This class represents a book in the database
    """
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    isbn = Column(String, unique=True, nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    user = relationship(Users, back_populates="books")

    def __repr__(self) -> str:
        return f"Book => {self.title}"
