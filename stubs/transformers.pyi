# transformers.pyi
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    # Assuming these classes are defined somewhere in the transformers library.
    class PreTrainedModel: ...
    class PreTrainedTokenizer: ...

else:
    PreTrainedModel = Any
    PreTrainedTokenizer = Any

class AutoModel:
    @staticmethod
    def from_pretrained(
        pretrained_model_name_or_path: str, *args: Any, **kwargs: Any
    ) -> PreTrainedModel: ...

class AutoTokenizer:
    @staticmethod
    def from_pretrained(
        pretrained_model_name_or_path: str, *args: Any, **kwargs: Any
    ) -> PreTrainedTokenizer: ...
