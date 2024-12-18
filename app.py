from fastapi import FastAPI
from contextlib import asynccontextmanager
from db.main import init_db
from errors import register_all_errors
from middleware import register_middleware
from auth.routes import auth_router
from book.routers import book_router
from reviews.routes import review_router
from tags.routes import tags_router


@asynccontextmanager
async def life_span(app: FastAPI):
    print("server is starting....")
    await init_db()
    yield
    print("server has been stopped")


version = "v1"
version_prefix = f"/api/{version}"

app = FastAPI(
    title="Login API",
    description="BECO POWERING SOMALIA",
    lifespan=life_span
)

register_all_errors(app)

register_middleware(app)

app.include_router(book_router, prefix=f"{version_prefix}/books", tags=["books"])
app.include_router(auth_router, prefix=f"{version_prefix}/auth", tags=["auth"])
app.include_router(review_router, prefix=f"{version_prefix}/reviews", tags=["reviews"])
app.include_router(tags_router, prefix=f"{version_prefix}/tags", tags=["tags"])
