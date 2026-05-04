#Add a global db connection here
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.core.config import config
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession


engine = create_async_engine(
    config.DATABASE_URL,
    echo=False,
    pool_size=10,
    max_overflow=20
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)


Base = declarative_base()

# Dependency for FastAPI
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()