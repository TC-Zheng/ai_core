import pytest
from unittest.mock import Mock, patch

from ai_core.api.request_models import DownloadAIModelRequest
from ai_core.service.download_ai_model_service import DownloadAIModelService
from ai_core.utils.llm_core_exception import (
    NetworkException,
    NotFoundException,
    UnknownException,
)


class TestDownloadLLMService:
    @patch("transformers.AutoTokenizer.from_pretrained")
    @patch("transformers.AutoModel.from_pretrained")
    def test_download_llm_success(self, mock_auto_model, mock_auto_tokenizer):
        # Mock
        mock_repository = Mock()
        mock_repository.save_llm.return_value = None
        service = DownloadAIModelService(repository=mock_repository)
        mock_auto_model.return_value = "mocked_model"
        mock_auto_tokenizer.return_value = "mocked_tokenizer"

        # Run and Assert
        service.download_llm(
            DownloadAIModelRequest(hugging_face_model_id="valid_model_id")
        )

        mock_repository.save_ai_model.assert_called_once_with(
            "mocked_model", "mocked_tokenizer", "valid_model_id"
        )

    @patch("transformers.AutoModel.from_pretrained")
    def test_download_llm_not_found_exception(self, mock_auto_model):
        # Mock
        mock_repository = Mock()
        mock_repository.save_llm.return_value = None
        service = DownloadAIModelService(repository=mock_repository)
        mock_auto_model.side_effect = Exception(
            "is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'"
        )

        # Run and Assert
        with pytest.raises(NotFoundException):
            service.download_llm(
                DownloadAIModelRequest(hugging_face_model_id="valid_model_id")
            )

    @patch("transformers.AutoModel.from_pretrained")
    def test_download_llm_network_exception(self, mock_auto_model):
        # Mock
        mock_repository = Mock()
        mock_repository.save_llm.return_value = None
        service = DownloadAIModelService(repository=mock_repository)
        mock_auto_model.side_effect = Exception(
            "We couldn't connect to 'https://huggingface.co' to download model"
        )

        # Run and Assert
        with pytest.raises(NetworkException):
            service.download_llm(
                DownloadAIModelRequest(hugging_face_model_id="valid_model_id")
            )

    @patch("transformers.AutoModel.from_pretrained")
    def test_download_llm_unknown_exception(self, mock_auto_model):
        # Mock
        mock_repository = Mock()
        mock_repository.save_llm.return_value = None
        service = DownloadAIModelService(repository=mock_repository)
        mock_auto_model.side_effect = Exception("Unexpected error")

        # Run and Assert
        with pytest.raises(UnknownException):
            service.download_llm(
                DownloadAIModelRequest(hugging_face_model_id="valid_model_id")
            )
