from pydantic import BaseModel


class DownloadAIModelResponse(BaseModel):
    success: bool
    message: str
