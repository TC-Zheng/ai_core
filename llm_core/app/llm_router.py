from fastapi import APIRouter, Depends

from llm_core.api.request_models import DownloadLLMRequest
from llm_core.api.response_models import DownloadLLMResponse
from llm_core.dependencies.llm_dependency import get_download_llm_service
from llm_core.service.download_llm_service import DownloadLLMService

router = APIRouter()


@router.post("/download_llm/")
async def download_llm(
    download_llm_request: DownloadLLMRequest,
    download_llm_service: DownloadLLMService = Depends(get_download_llm_service),
) -> DownloadLLMResponse:
    download_llm_service.download_llm(download_llm_request.hugging_face_model_id)

    return DownloadLLMResponse(success=True, message="Model downloaded successfully")
