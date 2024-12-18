from db.models import Book
from pydantic import BaseModel


class BookResponseModel(Book):
    """
This class is used to validate the response when getting book objects
    """
    pass


class BookCreateModel(BaseModel):
    """
This class is used to validate the request when creating or updating a book
    """
    title: str
    author: str
    isbn: str
    description: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Java Cookbook",
                "author": "Garaad Maxamed",
                "isbn": "265-5-9875-3564-9",
                "description": "Java Cookbook is a collection of books written by <NAME> and <NAME>.",
            }
        }
    }
