from transformers import AutoModel, AutoTokenizer

from llm_core.data_access.llm_repository import LLMRepository


class DownloadLLMService:
    def __init__(self, repository: LLMRepository) -> None:
        self.repository = repository

    def download_llm(self, huggingface_model_id: str) -> None:
        model = AutoModel.from_pretrained(huggingface_model_id)
        tokenizer = AutoTokenizer.from_pretrained(huggingface_model_id)

        self.repository.save_llm(model, tokenizer, huggingface_model_id)
