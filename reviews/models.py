from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from db.models import User
from db.models import Book
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# class Reviews(Base):
#     __tablename__ = "reviews"
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     rating = Column(Integer, nullable=False)
#     review_text = Column(String, nullable=False)
#     created_at = Column(DateTime, default=datetime.now, nullable=False)
#     update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
#
#     # Relationships (assuming User and Book models are defined elsewhere)
#     user_id = Column(Integer, ForeignKey('users.id'), index=True)
#     user = relationship(User, back_populates="reviews")
#     book_id = Column(Integer, ForeignKey('books.id'), index=True)
#     book = relationship(Book, back_populates="reviews")
#
#     def __repr__(self):
#         return f"<Review for book {self.book_id} by user {self.user_id}>"
