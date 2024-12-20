import datetime

from db.models import Book
from pydantic import BaseModel


class BookResponseModel(BaseModel):
    book: Book
    """ This class is used to validate the response when getting book objects """


class BookCreateModel(BaseModel):
    """
This class is used to validate the request when creating or updating a book
    """
    title: str
    author: str
    publisher: str
    published_date: datetime.date
    page_count: int
    language: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Java Cookbook",
                "author": "Garaad Maxamed",
                "isbn": "265-5-9875-3564-9",
                "description": "Java Cookbook is a collection of books written by <NAME> and <NAME>.",
                "publisher": "Garaad",
                "published_date": "2024-12-20",
                "page_count": 504,
                "language": "python"
            }
        }
    }
