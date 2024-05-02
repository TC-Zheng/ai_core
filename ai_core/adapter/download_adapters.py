from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from transformers import AutoModel, AutoTokenizer

from ai_core.api.request_models import DownloadHFModelRequest
from ai_core.dto.ai_model_dto import LanguageModelDTO
from ai_core.utils.ai_core_exception import (
    NetworkException,
    NotFoundException,
    UnknownException,
)


R = TypeVar("R")
D = TypeVar("D")


class BaseDownloadAdapter(ABC, Generic[R, D]):
    @abstractmethod
    def download(self, request: R) -> D:
        raise NotImplementedError("Each child class must implement this method")


class HFLangModelDownloadAdapter(
    BaseDownloadAdapter[DownloadHFModelRequest, LanguageModelDTO]
):
    def download(self, request: DownloadHFModelRequest) -> LanguageModelDTO:
        """
        Download a Language Model from Hugging Face
        """
        huggingface_model_id = request.hugging_face_model_id
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
        return LanguageModelDTO(
            name=huggingface_model_id, model=model, tokenizer=tokenizer
        )
