from transformers import PreTrainedModel, PreTrainedTokenizer

from ai_core.utils.config import Config


class AIModelRepository:
    def __init__(self, config: Config) -> None:
        self.database_url = config.DATABASE_URL
        self.llm_storage_path = config.LLM_STORAGE_PATH

    def save_ai_model(
        self,
        ai_model: PreTrainedModel,
        tokenizer: PreTrainedTokenizer,
        model_name: str,
    ) -> None:
        pass
