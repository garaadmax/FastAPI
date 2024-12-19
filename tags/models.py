from datetime import datetime
from sqlalchemy import Column, ForeignKey, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class BookTags(Base):
    __tablename__ = "book_tags"
    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey('books.id'), index=True)
    book = relationship("Books")
    tag_id = Column(Integer, ForeignKey('tags.id'), index=True)
    tag = relationship("Tag")


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    # Many-to-many relationship with Book via BookTag
    book_id = Column(Integer, ForeignKey('books.id'), index=True)
    book = relationship("Books")

    def __repr__(self) -> str:
        return f"<Tag {self.name}>"
