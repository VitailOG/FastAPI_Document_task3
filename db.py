from sqlalchemy import (
    PrimaryKeyConstraint,
    Index,
    Column,
    Identity,
    Integer,
    Text,
    Date,
    String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import ARRAY

engine = create_async_engine(
    'postgresql+asyncpg://postgres:vzakharkiv2018@localhost:5432/fastapi',
    echo=True
)

async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session


class Document(Base):
    __tablename__ = "document"

    id = Column(Integer, Identity())
    text = Column(Text, nullable=False)
    created_date = Column(Date, nullable=False)
    rubrics = Column(ARRAY(String))

    __table_args__ = (
        PrimaryKeyConstraint("id"),
        Index('text_idx', 'text')
    )
