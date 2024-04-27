from transformers import PreTrainedModel, PreTrainedTokenizer

from llm_core.utils.config import Config


class LLMRepository:
    def __init__(self, config: Config) -> None:
        self.database_url = config.DATABASE_URL
        self.llm_storage_path = config.LLM_STORAGE_PATH

    def save_llm(
        self,
        llm: PreTrainedModel,
        tokenizer: PreTrainedTokenizer,
        model_name: str,
    ) -> None:
        pass
