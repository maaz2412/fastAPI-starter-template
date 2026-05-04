#Add a global db connection here
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.core.config import config


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