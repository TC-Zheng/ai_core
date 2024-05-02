import pytest
from unittest.mock import Mock
from pydantic import BaseModel
from ai_core.adapter.download_adapters import BaseDownloadAdapter
from ai_core.data_access.repository_base import RepositoryBase
from ai_core.service.download_ai_model_service import DownloadAIModelService


class TestDownloadAIModelService:
    @pytest.fixture
    def mock_download_adapter(self):
        return Mock(spec=BaseDownloadAdapter)

    @pytest.fixture
    def mock_repository(self):
        return Mock(spec=RepositoryBase)

    @pytest.fixture
    def service(self, mock_download_adapter, mock_repository):
        return DownloadAIModelService(mock_download_adapter, mock_repository)

    def test_download_and_save(self, service, mock_download_adapter, mock_repository):
        mock_request = Mock(spec=BaseModel)
        mock_ai_model = Mock()

        mock_download_adapter.download.return_value = mock_ai_model
        mock_repository.create.return_value = None

        service.download_and_save(mock_request)

        mock_download_adapter.download.assert_called_once_with(mock_request)
        mock_repository.create.assert_called_once_with(mock_ai_model)
