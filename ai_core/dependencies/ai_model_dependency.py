from fastapi import Depends

from ai_core.data_access.ai_model_repository import AIModelRepository
from ai_core.service.download_ai_model_service import DownloadAIModelService
from ai_core.utils.config import get_config, Config


def get_llm_repository(config: Config = Depends(get_config)) -> AIModelRepository:
    return AIModelRepository(config)


def get_download_ai_model_service(
    repository: AIModelRepository = Depends(get_llm_repository),
) -> DownloadAIModelService:
    return DownloadAIModelService(repository)
