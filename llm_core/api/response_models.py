from pydantic import BaseModel


class DownloadLLMResponse(BaseModel):
    success: bool
    message: str
