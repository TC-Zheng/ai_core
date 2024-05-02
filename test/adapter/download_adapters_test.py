import pytest
from unittest.mock import patch, Mock
from transformers import AutoModel, AutoTokenizer
from ai_core.adapter.download_adapters import (
    HFLangModelDownloadAdapter,
    DownloadHFModelRequest,
    NotFoundException,
    NetworkException,
    UnknownException,
)


@patch.object(AutoModel, "from_pretrained")
@patch.object(AutoTokenizer, "from_pretrained")
def test_download(mock_tokenizer, mock_model):
    adapter = HFLangModelDownloadAdapter()
    request = DownloadHFModelRequest(hugging_face_model_id="bert-base-uncased")

    # Test successful download
    mock_model.return_value = Mock()
    mock_tokenizer.return_value = Mock()
    result = adapter.download(request)
    assert result.model is not None
    assert result.tokenizer is not None
    assert result.name == "bert-base-uncased"
    # Test model not found
    mock_model.side_effect = Exception(
        "is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'"
    )
    with pytest.raises(NotFoundException):
        adapter.download(request)

    # Test network exception
    mock_model.side_effect = Exception(
        "We couldn't connect to 'https://huggingface.co' to download model"
    )
    with pytest.raises(NetworkException):
        adapter.download(request)

    # Test unknown exception
    mock_model.side_effect = Exception("Unknown error")
    with pytest.raises(UnknownException):
        adapter.download(request)
