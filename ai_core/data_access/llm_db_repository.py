from sqlalchemy.ext.asyncio import AsyncSession

from ai_core.data_access.db_transaction import db_transaction
from ai_core.dto.ai_model_dto import LargeLanguageModelDTO
from ai_core.utils.app_config import AppConfig
from ai_core.data_access.repository_base import DBRepositoryBase


class LLMDatabaseRepository(DBRepositoryBase):
    def __init__(self, appConfig: AppConfig, async_session: AsyncSession) -> None:
        self.database_url = appConfig.DATABASE_URL
        self.llm_storage_path = appConfig.FILE_STORAGE_PATH

    @db_transaction
    def save(self, ai_model_dto: LargeLanguageModelDTO) -> None:
        ai_model_dto.model.save_pretrained(self.llm_storage_path)
        ai_model_dto.tokenizer.save_pretrained(self.llm_storage_path)
