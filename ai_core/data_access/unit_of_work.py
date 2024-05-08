from sqlalchemy.ext.asyncio import AsyncSession

from ai_core.data_access.llm_db_repository import LLMDatabaseRepository


class UnitOfWork:
    """Manages a group of repositories under a single transactional context."""

    def __init__(self, session: AsyncSession):
        self.session = session
        # Add other repositories as needed

    async def __aenter__(self) -> "UnitOfWork":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        try:
            if exc_type:
                raise exc_val
            else:
                await self.session.commit()
        except Exception as e:
            await self.session.rollback()
            raise e
        finally:
            await self.session.close()

    def create_llm_db_repository(self):
        return LLMDatabaseRepository(self.session)
