import uuid
from transformers import PreTrainedModel, PreTrainedTokenizer
from ai_core.utils.app_config import appConfig


def save_hf_llm_to_file(llm: PreTrainedModel, tokenizer: PreTrainedTokenizer):
    path = appConfig.FILE_STORAGE_PATH + str(uuid.uuid4())
    llm.save_pretrained(path)
    tokenizer.save_pretrained(path)
    return path


def load_hf_llm_from_file(path: str) -> tuple[PreTrainedModel, PreTrainedTokenizer]:
    return (
        PreTrainedModel.from_pretrained(path),
        PreTrainedTokenizer.from_pretrained(path),
    )
