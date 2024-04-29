from transformers import AutoModel, AutoTokenizer

from ai_core.data_access.ai_model_repository import AIModelRepository
from ai_core.api.request_models import DownloadAIModelRequest
from ai_core.utils.llm_core_exception import (
    NetworkException,
    NotFoundException,
    UnknownException,
)


class DownloadAIModelService:
    def __init__(
        self,
        repository: AIModelRepository,
    ) -> None:
        self.repository = repository

    def download_llm(self, download_ai_model_request: DownloadAIModelRequest) -> None:
        """
        Download a Language Model from Hugging Face
        """
        huggingface_model_id = download_ai_model_request.hugging_face_model_id
        try:
            model = AutoModel.from_pretrained(huggingface_model_id)
            tokenizer = AutoTokenizer.from_pretrained(huggingface_model_id)
        except Exception as e:
            msg = str(e)
            if (
                "is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'"
                in msg
            ):
                raise NotFoundException("Model not found on Hugging Face")
            elif (
                "We couldn't connect to 'https://huggingface.co' to download model"
                in msg
            ):
                raise NetworkException("Couldn't connect to Hugging Face")
            else:
                raise UnknownException(
                    "Unknown error occurred when downloading model from Hugging Face"
                )

        self.repository.save_ai_model(model, tokenizer, huggingface_model_id)
