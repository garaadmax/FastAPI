from fastapi import FastAPI
from root.book.routes import book_router
from contextlib import asynccontextmanager
from root.database.main import init_db

@asynccontextmanager
async def life_span(app: FastAPI):
    print("Server is starting...")
    init_db()
    yield
    print("Server is stopping...")

version ="v1"
app = FastAPI(
    title="Book API",
    description="A Rest API for a book API review web service",
    version=version,
    life_span=life_span,
)
app.include_router(book_router,prefix=f"/api/{version}/books", tags=["book"])
