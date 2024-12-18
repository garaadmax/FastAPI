import uuid
from datetime import datetime
from sqlalchemy import Column, ForeignKey, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class BookTags(Base):
    __tablename__ = "book_tags"

    book_id = Column(UUID(as_uuid=True), ForeignKey("books.uid"), primary_key=True)
    tag_id = Column(UUID(as_uuid=True), ForeignKey("tags.uid"), primary_key=True)


class Tag(Base):
    __tablename__ = "tags"

    uid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    # Many-to-many relationship with Book via BookTag
    books = relationship(
        "Book",
        secondary="book_tags",
        back_populates="tags",
        lazy="selectin"
    )

    def __repr__(self) -> str:
        return f"<Tag {self.name}>"

