from fastapi import Depends

from llm_core.data_access.llm_repository import LLMRepository
from llm_core.service.download_llm_service import DownloadLLMService
from llm_core.utils.config import get_config, Config


def get_llm_repository(config: Config = Depends(get_config)) -> LLMRepository:
    return LLMRepository(config)


def get_download_llm_service(
    repository: LLMRepository = Depends(get_llm_repository),
) -> DownloadLLMService:
    return DownloadLLMService(repository)
