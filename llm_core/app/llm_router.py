from fastapi import APIRouter, Depends
from typing import Callable

from llm_core.api.request_models import DownloadLLMRequest
from llm_core.api.response_models import DownloadLLMResponse
from llm_core.dependencies.llm_dependency import get_download_llm

router = APIRouter()


@router.post("/download_llm/")
async def download_llm(
    download_llm_request: DownloadLLMRequest,
    download_llm: Callable[[str], None] = Depends(get_download_llm),
) -> DownloadLLMResponse:
    download_llm(download_llm_request.hugging_face_model_id)

    return DownloadLLMResponse(success=True, message="Model downloaded successfully")
