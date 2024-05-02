from ai_core.dto.ai_model_dto import LanguageModelDTO
from ai_core.utils.app_config import AppConfig
from ai_core.data_access.repository_base import RepositoryBase


class HFLangModelRepository(RepositoryBase[LanguageModelDTO]):
    def __init__(self, config: AppConfig) -> None:
        self.database_url = config.DATABASE_URL
        self.llm_storage_path = config.LLM_STORAGE_PATH

    def save(self, ai_model: LanguageModelDTO) -> None:
        ai_model.model.save_pretrained(self.llm_storage_path)
        ai_model.tokenizer.save_pretrained(self.llm_storage_path)
