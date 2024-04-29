import unittest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock

import pytest

from ai_core.api.request_models import DownloadAIModelRequest
from ai_core.app.main import app
from ai_core.service.download_ai_model_service import DownloadAIModelService
from ai_core.app.ai_router import get_download_ai_model_service


@pytest.fixture(scope="class")
def client(request):
    client = TestClient(app)
    request.cls.client = client  # Set the client as a class attribute


@pytest.mark.usefixtures("client")
class TestDownloadLLM:
    def test_valid_request_return_success(self):
        # Mock
        mock_service = MagicMock(spec=DownloadAIModelService)
        mock_service.download_llm.return_value = None
        app.dependency_overrides[get_download_ai_model_service] = lambda: mock_service

        # Run and Assert
        response = self.client.post(
            "/download_ai_model/",
            json={"hugging_face_model_id": "gpt2"},
        )

        assert response.status_code == 200
        assert response.json() == {
            "success": True,
            "message": "Model downloaded successfully",
        }

        mock_service.download_llm.assert_called_once_with(
            DownloadAIModelRequest(hugging_face_model_id="gpt2")
        )

    def test_invalid_request_return_error(self):
        # Run and Assert
        response = self.client.post(
            "/download_ai_model/",
            json={"hugging_face_model_id_2": "gpt2"},
        )
        assert response.status_code == 422
        assert response.json() == {
            "detail": [
                {
                    "input": {"hugging_face_model_id_2": "gpt2"},
                    "loc": ["body", "hugging_face_model_id"],
                    "msg": "Field required",
                    "type": "missing",
                }
            ]
        }


if __name__ == "__main__":
    unittest.main()
