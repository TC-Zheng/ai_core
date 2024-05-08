from fastapi import Depends

from ai_core.adapter.download_adapters import (
    HFLangModelDownloadAdapter,
)
from ai_core.data_access.llm_db_repository import HFLangModelRepository
from ai_core.service.download_ai_model_service import DownloadAIModelService
from ai_core.utils.app_config import get_app_config, AppConfig


def get_hf_lang_model_repository(
    config: AppConfig = Depends(get_app_config),
) -> HFLangModelRepository:
    return HFLangModelRepository(config)


def get_hf_lang_model_download_adapter() -> HFLangModelDownloadAdapter:
    return HFLangModelDownloadAdapter()


def get_download_hf_lang_model_service(
    download_adapter: HFLangModelDownloadAdapter = Depends(
        get_hf_lang_model_download_adapter
    ),
    repository: HFLangModelRepository = Depends(get_hf_lang_model_repository),
) -> DownloadAIModelService:
    return DownloadAIModelService(download_adapter, repository)
