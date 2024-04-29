from fastapi import APIRouter, Depends

from ai_core.api.request_models import DownloadAIModelRequest
from ai_core.api.response_models import DownloadAIModelResponse
from ai_core.dependencies.ai_model_dependency import get_download_ai_model_service
from ai_core.service.download_ai_model_service import DownloadAIModelService

router = APIRouter()


@router.post("/download_ai_model/")
async def download_ai_model(
    download_ai_model_request: DownloadAIModelRequest,
    download_ai_model_service: DownloadAIModelService = Depends(
        get_download_ai_model_service
    ),
) -> DownloadAIModelResponse:
    """
    Download a Language Model based on it's name (id)
    """
    download_ai_model_service.download_llm(download_ai_model_request)

    return DownloadAIModelResponse(
        success=True, message="Model downloaded successfully"
    )
