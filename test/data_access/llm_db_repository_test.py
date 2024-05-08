import pytest
from ai_core.data_access.llm_db_repository import LLMDatabaseRepository
from sqlalchemy.ext.asyncio import create_async_engine


@pytest.fixture(scope="module")
async def db_session():
    engine = create_async_engine("sqlite+aiosqlite:///:memory:", echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Create a sessionmaker factory
    async_session_factory = sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
    )

    # Yield session
    async with async_session_factory() as session:
        yield session

    await engine.dispose()
