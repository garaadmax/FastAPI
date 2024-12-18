import uuid
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Reviews(Base):
    __tablename__ = "reviews"

    uid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    rating = Column(Integer, nullable=False)
    review_text = Column(String, nullable=False)
    user_uid = Column(UUID(as_uuid=True), ForeignKey("users.uid"), nullable=True)
    book_uid = Column(UUID(as_uuid=True), ForeignKey("books.uid"), nullable=True)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    # Relationships (assuming User and Book models are defined elsewhere)
    user = relationship("User", back_populates="reviews")
    book = relationship("Book", back_populates="reviews")

    def __repr__(self):
        return f"<Review for book {self.book_uid} by user {self.user_uid}>"
