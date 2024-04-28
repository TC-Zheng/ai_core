from transformers import PreTrainedModel, PreTrainedTokenizer

from llm_core.utils.config import Config


def save_llm_and_metadata(
    llm: PreTrainedModel,
    tokenizer: PreTrainedTokenizer,
    model_name: str,
    config: Config,
) -> None:
    config.LLM_STORAGE_PATH
    config.DATABASE_URL
