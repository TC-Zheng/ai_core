from typing import TypeVar
from pydantic import BaseModel

from ai_core.adapter.download_adapters import BaseDownloadAdapter
from ai_core.data_access.repository_base import RepositoryBase
from ai_core.api.request_models import BaseRequest

T = TypeVar("T", bound=BaseRequest)
S = TypeVar("S", bound=BaseModel)


class DownloadAIModelService:
    def __init__(
        self,
        download_adapter: BaseDownloadAdapter[T, S],
        repository: RepositoryBase[S],
    ) -> None:
        self.download_adapter = download_adapter
        self.repository = repository

    def download_and_save(self, download_ai_model_request: T) -> None:
        ai_model = self.download_adapter.download(download_ai_model_request)
        self.repository.create(ai_model)
