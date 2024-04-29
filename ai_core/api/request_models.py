from pydantic import BaseModel


class DownloadAIModelRequest(BaseModel):
    hugging_face_model_id: str
