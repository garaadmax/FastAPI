from typing import Optional
from typing import List
from fastapi import APIRouter, Header, Request, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, Field
from root.book.schemas import BookCreateModel, Books, books

book_router = APIRouter()


@book_router.get('/greet/{name}')
async def greet(name: str) -> dict:
    return {"massege": f"yasir alle {name}"}


@book_router.get('/greet/')
async def greet(name: Optional[str] = "Jimcaale", age: int = 0) -> dict:
    return {"massege": f"yasir alle {name}", "age": age}


@book_router.post('/create_book')
async def create_book(book_data: BookCreateModel):
    return {"title": book_data.title, "author": book_data.author}


@book_router.get('/get_headers')
async def get_headers(accept: str = Header(None), content_type: str = Header(None)):
    print(Header())
    request_headers = {}
    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type
    return request_headers


@book_router.get("/all-headers/", status_code=200)
async def get_all_headers(request: Request):
    headers = request.headers  # Access all headers
    return {"headers": dict(headers)}  # Convert to dictionary for display


@book_router.get('/', response_model=List[Books])
async def get_all_books():
    return books


@book_router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_books(book_data: Books) -> dict:  # Use Books as the type of request body
    new_book = book_data.model_dump()  # Call model_dump() on the instance
    books.append(new_book)  # Add the new book to the in-memory storage
    return {"message": "Book added successfully", "book": new_book}


@book_router.patch('/update/{book_id}', status_code=status.HTTP_201_CREATED)
async def update_books(book_id: int, book_data: Books) -> dict:
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_data.title
            book['author'] = book_data.author
            book['year'] = book_data.year
            book['genres'] = book_data.genres
            book['isbn'] = book_data.isbn
            book['publisher'] = book_data.publisher
            book['publisher_date'] = book_data.published_date
            book['page_count'] = book_data.page_count
            book['language'] = book_data.language
            return {"message": "Book update successfully", "book": book}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@book_router.delete('/delete/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_books(book_id: int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return {"message": "Book deleted successfully", "book": book}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@book_router.get('/{book_id}', status_code=status.HTTP_200_OK)
async def get_book(book_id: int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
