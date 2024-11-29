from typing import List

from pydantic import Field, BaseModel


class BookCreateModel(BaseModel):
    title: str = Field(..., max_length=3)
    author: str = Field(..., min_length=3)


book_records = [
    {
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
        "genres": ["Dystopian", "Political Fiction"],
        "isbn": "123-1234567890",
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": 1960,
        "genres": ["Classic", "Historical Fiction"],
        "isbn": "123-1234567891",
    },
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925,
        "genres": ["Classic", "Tragedy"],
        "isbn": "123-1234567892",
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "year": 1813,
        "genres": ["Romance", "Classic"],
        "isbn": "123-1234567893",
    },
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "year": 1937,
        "genres": ["Fantasy", "Adventure"],
        "isbn": "123-1234567894",
    },
    {
        "title": "Brave New World",
        "author": "Aldous Huxley",
        "year": 1932,
        "genres": ["Dystopian", "Science Fiction"],
        "isbn": "123-1234567895",
    },
    {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "year": 1951,
        "genres": ["Classic", "Coming-of-Age"],
        "isbn": "123-1234567896",
    },
]
books = [
    {
        "id":1,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": 1960,
        "genres": ["Fiction", "Classic"],
        "isbn": "978-0061120084",
        "publisher": "J.B. Lippincott & Co.",
        "published_date": "1960-07-11",
        "page_count": 281,
        "language": "English"
    },
    {
        "id": 2,
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
        "genres": ["Dystopian", "Political Fiction"],
        "isbn": "978-0451524935",
        "publisher": "Secker & Warburg",
        "published_date": "1949-06-08",
        "page_count": 328,
        "language": "English"
    },
    {
        "id": 3,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "year": 1813,
        "genres": ["Romance", "Classic"],
        "isbn": "978-0141439518",
        "publisher": "T. Egerton, Whitehall",
        "published_date": "1813-01-28",
        "page_count": 279,
        "language": "English"
    },
    {
        "id": 4,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925,
        "genres": ["Fiction", "Classic"],
        "isbn": "978-0743273565",
        "publisher": "Charles Scribner's Sons",
        "published_date": "1925-04-10",
        "page_count": 180,
        "language": "English"
    },
    {
        "id": 5,
        "title": "Moby Dick",
        "author": "Herman Melville",
        "year": 1851,
        "genres": ["Adventure", "Classic"],
        "isbn": "978-1503280786",
        "publisher": "Harper & Brothers",
        "published_date": "1851-11-14",
        "page_count": 585,
        "language": "English"
    },
    {
        "id": 6,
        "title": "War and Peace",
        "author": "Leo Tolstoy",
        "year": 1869,
        "genres": ["Historical Fiction", "Classic"],
        "isbn": "978-0199232765",
        "publisher": "The Russian Messenger",
        "published_date": "1869",
        "page_count": 1225,
        "language": "Russian"
    },
    {
        "id": 7,
        "title": "Crime and Punishment",
        "author": "Fyodor Dostoevsky",
        "year": 1866,
        "genres": ["Philosophical Fiction", "Classic"],
        "isbn": "978-0140449136",
        "publisher": "The Russian Messenger",
        "published_date": "1866",
        "page_count": 430,
        "language": "Russian"
    },
    {
        "id": 8,
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "year": 1951,
        "genres": ["Fiction", "Coming-of-Age"],
        "isbn": "978-0316769488",
        "publisher": "Little, Brown and Company",
        "published_date": "1951-07-16",
        "page_count": 277,
        "language": "English"
    },
    {
        "id": 9,
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "year": 1937,
        "genres": ["Fantasy", "Adventure"],
        "isbn": "978-0547928227",
        "publisher": "George Allen & Unwin",
        "published_date": "1937-09-21",
        "page_count": 310,
        "language": "English"
    },
    {
        "id": 10,
        "title": "Ulysses",
        "author": "James Joyce",
        "year": 1922,
        "genres": ["Modernist", "Classic"],
        "isbn": "978-0199535675",
        "publisher": "Sylvia Beach",
        "published_date": "1922-02-02",
        "page_count": 730,
        "language": "English"
    },
    {
        "id": 11,
        "title": "The Odyssey",
        "author": "Homer",
        "year": -700,
        "genres": ["Epic", "Poetry"],
        "isbn": "978-0140268867",
        "publisher": "Ancient Greece",
        "published_date": "Approx. 8th Century BCE",
        "page_count": 541,
        "language": "Ancient Greek"
    },
    {
        "id": 12,
        "title": "Don Quixote",
        "author": "Miguel de Cervantes",
        "year": 1605,
        "genres": ["Adventure", "Classic"],
        "isbn": "978-0060934347",
        "publisher": "Francisco de Robles",
        "published_date": "1605-01-16",
        "page_count": 1072,
        "language": "Spanish"
    },
    {
        "id": 13,
        "title": "Jane Eyre",
        "author": "Charlotte Brontë",
        "year": 1847,
        "genres": ["Gothic", "Romance"],
        "isbn": "978-0142437209",
        "publisher": "Smith, Elder & Co.",
        "published_date": "1847-10-16",
        "page_count": 500,
        "language": "English"
    },
    {
        "id": 14,
        "title": "Wuthering Heights",
        "author": "Emily Brontë",
        "year": 1847,
        "genres": ["Gothic", "Classic"],
        "isbn": "978-0141439556",
        "publisher": "Thomas Cautley Newby",
        "published_date": "1847-12-01",
        "page_count": 416,
        "language": "English"
    },
    {
        "id": 15,
        "title": "Brave New World",
        "author": "Aldous Huxley",
        "year": 1932,
        "genres": ["Dystopian", "Science Fiction"],
        "isbn": "978-0060850524",
        "publisher": "Chatto & Windus",
        "published_date": "1932-08-18",
        "page_count": 268,
        "language": "English"
    },
    {
        "id": 16,
        "title": "Anna Karenina",
        "author": "Leo Tolstoy",
        "year": 1877,
        "genres": ["Fiction", "Romance"],
        "isbn": "978-0140449174",
        "publisher": "The Russian Messenger",
        "published_date": "1877",
        "page_count": 864,
        "language": "Russian"
    },
    {
        "id": 17,
        "title": "The Divine Comedy",
        "author": "Dante Alighieri",
        "year": 1320,
        "genres": ["Epic", "Poetry"],
        "isbn": "978-0140448955",
        "publisher": "Ancient Italy",
        "published_date": "1320",
        "page_count": 798,
        "language": "Italian"
    },
    {
        "id": 18,
        "title": "The Lord of the Rings",
        "author": "J.R.R. Tolkien",
        "year": 1954,
        "genres": ["Fantasy", "Adventure"],
        "isbn": "978-0544003415",
        "publisher": "George Allen & Unwin",
        "published_date": "1954-07-29",
        "page_count": 1178,
        "language": "English"
    },
    {
        "id": 19,
        "title": "One Hundred Years of Solitude",
        "author": "Gabriel García Márquez",
        "year": 1967,
        "genres": ["Magic Realism", "Fiction"],
        "isbn": "978-0060883287",
        "publisher": "Harper & Row",
        "published_date": "1967-05-30",
        "page_count": 417,
        "language": "Spanish"
    },
    {
        "id": 20,
        "title": "The Brothers Karamazov",
        "author": "Fyodor Dostoevsky",
        "year": 1880,
        "genres": ["Philosophical Fiction", "Classic"],
        "isbn": "978-0374528379",
        "publisher": "The Russian Messenger",
        "published_date": "1880",
        "page_count": 824,
        "language": "Russian"
    }
]


class Book(BaseModel):
    title: str = Field(..., min_length=1, description="Title of the book")
    author: str = Field(..., min_length=1, description="Author of the book")
    year: int = Field(..., ge=0, le=2100, description="Publication year")
    genres: List[str] = Field(default_factory=list, description="List of genres")
    isbn: str = Field(..., pattern=r"^\d{3}-\d{10}$", description="ISBN of the book")


class Books(BaseModel):
    id: int
    title: str
    author: str
    year: int
    genres: List[str]
    isbn: str
    publisher: str
    published_date: str
    page_count: int
    language: str