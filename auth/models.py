from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, VARCHAR
from sqlalchemy.orm import relationship, declarative_base
import uuid
from datetime import datetime
# from typing import List
#
# import sqlalchemy.dialects.postgresql as pg
# from sqlmodel import  Field, Relationship, SQLModel
# from book.models import Book
# from reviews.models import Review






Base = declarative_base()

class Users(Base):
    __tablename__ = "users"

    uid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    role = Column(VARCHAR, nullable=False, server_default="user")
    is_verified = Column(Boolean, default=False)
    password_hash = Column(VARCHAR, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now)

    # Relationships
    books = relationship("Book", back_populates="user", lazy="selectin")
    reviews = relationship("Review", back_populates="user", lazy="selectin")

    def __repr__(self):
        return f"<User {self.username}>"


