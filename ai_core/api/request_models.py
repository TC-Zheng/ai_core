from pydantic import BaseModel


class BaseRequest(BaseModel):
    pass


class DownloadHFModelRequest(BaseRequest):
    hugging_face_model_id: str
