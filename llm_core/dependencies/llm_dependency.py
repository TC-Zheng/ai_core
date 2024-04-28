from fastapi import Depends
from transformers import PreTrainedModel, PreTrainedTokenizer, AutoModel, AutoTokenizer
from typing import Callable
from functools import partial

from llm_core.data_access.llm_repository import save_llm_and_metadata
from llm_core.service.download_llm_service import download_llm
from llm_core.utils.config import get_config, Config


def get_save_llm_and_metadata(
    config: Config = Depends(get_config),
) -> Callable[[PreTrainedModel, PreTrainedTokenizer, str], None]:
    return partial(save_llm_and_metadata, config=config)


def get_download_model() -> Callable[[str], PreTrainedModel]:
    return AutoModel.from_pretrained


def get_download_tokenizer() -> Callable[[str], PreTrainedTokenizer]:
    return AutoTokenizer.from_pretrained


def get_download_llm(
    save_llm: Callable[[PreTrainedModel, PreTrainedTokenizer, str], None] = Depends(
        get_save_llm_and_metadata
    ),
    download_model: Callable[[str], PreTrainedModel] = Depends(get_download_model),
    download_tokenizer: Callable[[str], PreTrainedTokenizer] = Depends(
        get_download_tokenizer
    ),
) -> Callable[[str], None]:
    return partial(
        download_llm,
        save_llm=save_llm,
        download_model=download_model,
        download_tokenizer=download_tokenizer,
    )
