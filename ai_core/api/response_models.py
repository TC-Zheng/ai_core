from pydantic import BaseModel


class DownloadHFModelResponse(BaseModel):
    success: bool
    message: str
