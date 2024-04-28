from fastapi.testclient import TestClient
from unittest.mock import MagicMock

from llm_core.app.main import app
from llm_core.service.download_llm_service import DownloadLLMService
from llm_core.app.llm_router import get_download_llm_service


def test_download_llm():
    mock_service = MagicMock(spec=DownloadLLMService)
    mock_service.download_llm.return_value = None
    app.dependency_overrides[get_download_llm_service] = lambda: mock_service

    client = TestClient(app)

    response = client.post(
        "/download_llm",
        json={"hugging_face_model_id": "gpt2"},
    )
    # assert response.status_code == 200
    assert response.json() == {
        "success": True,
        "message": "Model downloaded successfully",
    }

    mock_service.download_llm.assert_called_once_with("gpt2")
