from pydantic import BaseModel


class DownloadLLMRequest(BaseModel):
    hugging_face_model_id: str
