from fastapi import Depends
from transformers import PreTrainedModel, PreTrainedTokenizer, AutoModel, AutoTokenizer
from typing import Callable

from llm_core.data_access.llm_repository import LLMRepository
from llm_core.service.download_llm_service import DownloadLLMService
from llm_core.utils.config import get_config, Config


def get_llm_repository(config: Config = Depends(get_config)) -> LLMRepository:
    return LLMRepository(config)


def get_download_model() -> Callable[[str], PreTrainedModel]:
    return AutoModel.from_pretrained


def get_download_tokenizer() -> Callable[[str], PreTrainedTokenizer]:
    return AutoTokenizer.from_pretrained


def get_download_llm_service(
    repository: LLMRepository = Depends(get_llm_repository),
    download_model: Callable[[str], PreTrainedModel] = Depends(get_download_model),
    download_tokenizer: Callable[[str], PreTrainedTokenizer] = Depends(
        get_download_tokenizer
    ),
) -> DownloadLLMService:
    return DownloadLLMService(repository, download_model, download_tokenizer)
