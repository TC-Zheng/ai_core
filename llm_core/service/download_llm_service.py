from transformers import PreTrainedModel, PreTrainedTokenizer
from typing import Callable


def download_llm(
    huggingface_model_id: str,
    download_model: Callable[[str], PreTrainedModel],
    download_tokenizer: Callable[[str], PreTrainedTokenizer],
    save_llm: Callable[[PreTrainedModel, PreTrainedTokenizer, str], None],
) -> None:
    model = download_model(huggingface_model_id)
    tokenizer = download_tokenizer(huggingface_model_id)

    save_llm(model, tokenizer, huggingface_model_id)
