from datetime import datetime
from sqlalchemy import Column, String, Boolean, DateTime, Integer
from sqlalchemy.dialects.postgresql import VARCHAR
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    role = Column(VARCHAR, nullable=False, server_default="user")
    is_verified = Column(Boolean, default=False)
    password_hash = Column(VARCHAR, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f"<User {self.username}>"
