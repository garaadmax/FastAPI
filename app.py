from fastapi import FastAPI
from login import routers
from book.routers import book_router
from contextlib import asynccontextmanager
from db.main import init_db

@asynccontextmanager
async def life_span(app: FastAPI):
    print("server is starting....")
    await init_db()
    yield
    print("server has been stopped")


app = FastAPI(
    title="Login API",
    docs_url="/grd",
    description="BECO POWERING SOMALIA",
    lifespan=life_span
)

app.include_router(routers.router)
app.include_router(book_router)
