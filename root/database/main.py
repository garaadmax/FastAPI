from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from root.config import config

engine = AsyncEngine(create_engine(url=config.DATABASE_URL, echo=True, ))

# async_engine = create_async_engine(url=config.DATABASE_URL, echo=True, )

async def init_db():
    async with engine.begin() as conn:
        stmt = text("SELECT 'Hello';")
        result = await conn.execute(stmt)
        print(result.fetchall())
