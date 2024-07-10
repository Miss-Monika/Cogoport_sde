# from sqlalchemy import create_engine, MetaData
# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.schema import Table

# DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost/config_db"

# # Create both async and sync engines
# async_engine = create_async_engine(DATABASE_URL, echo=True)
# sync_engine = create_engine(DATABASE_URL.replace("+asyncpg", ""), echo=True)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession)

# # Create a MetaData instance
# metadata = MetaData()

# # reflect db schema to MetaData
# metadata.reflect(bind=sync_engine)

# async def get_db():
#     async with SessionLocal() as session:
#         yield session

# # Create all tables
# def create_tables():
#     with sync_engine.begin() as connection:
#         metadata.create_all(connection)

# engine = sync_engine

# # Call the function to create tables
# create_tables()

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker



# Create both async and sync engines
async_engine = create_async_engine(DATABASE_URL, echo=True)
sync_engine = create_engine(DATABASE_URL.replace("+asyncpg", ""), echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession)

# Create a MetaData instance
metadata = MetaData()

async def get_db():
    async with SessionLocal() as session:
        yield session

# Create all tables
def create_tables():
    with sync_engine.begin() as connection:
        metadata.create_all(connection)

engine = sync_engine

# Call the function to create tables
create_tables()
