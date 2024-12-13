from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import text, SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from config import Config as settings

async_engine = create_async_engine(url=settings.database_url, echo=True)


async_session = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def init_db():
    """Create the database tables"""
    async with async_engine.begin() as conn:
        from book.models import Book
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    """Dependency to provide the session object"""
    async with async_session() as session:
        yield session