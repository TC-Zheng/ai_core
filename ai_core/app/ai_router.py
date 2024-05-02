from fastapi import APIRouter, Depends

from ai_core.api.request_models import DownloadHFModelRequest
from ai_core.api.response_models import DownloadHFModelResponse
from ai_core.dependencies.ai_model_dependency import get_download_hf_lang_model_service
from ai_core.service.download_ai_model_service import DownloadAIModelService

router = APIRouter()


@router.post("/download/hf_lang_model/")
async def download_ai_model(
    download_ai_model_request: DownloadHFModelRequest,
    download_ai_model_service: DownloadAIModelService = Depends(
        get_download_hf_lang_model_service
    ),
) -> DownloadHFModelResponse:
    """
    Download a Language Model based on it's name (id)
    """
    download_ai_model_service.download_and_save(download_ai_model_request)

    return DownloadHFModelResponse(
        success=True, message="Model downloaded successfully"
    )
