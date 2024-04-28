from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from typing import Callable

from llm_core.app.main import app
from llm_core.app.llm_router import get_download_llm


def test_download_llm():
    mock_function = MagicMock(Callable[[str], None])
    mock_function.return_value = None
    app.dependency_overrides[get_download_llm] = lambda: mock_function

    client = TestClient(app)

    response = client.post(
        "/download_llm",
        json={"hugging_face_model_id": "gpt2"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "success": True,
        "message": "Model downloaded successfully",
    }

    mock_function.assert_called_once_with("gpt2")


test_download_llm()
