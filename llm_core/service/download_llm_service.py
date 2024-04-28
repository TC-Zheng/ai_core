from transformers import PreTrainedModel, PreTrainedTokenizer
from typing import Callable

from llm_core.data_access.llm_repository import LLMRepository


class DownloadLLMService:
    def __init__(
        self,
        repository: LLMRepository,
        download_model: Callable[[str], PreTrainedModel],
        download_tokenizer: Callable[[str], PreTrainedTokenizer],
    ) -> None:
        self.repository = repository
        self.download_model = download_model
        self.download_tokenizer = download_tokenizer

    def download_llm(self, huggingface_model_id: str) -> None:
        model = self.download_model(huggingface_model_id)
        tokenizer = self.download_tokenizer(huggingface_model_id)

        self.repository.save_llm(model, tokenizer, huggingface_model_id)
