from pydantic import BaseModel

class LargeLanguageModelDTO(BaseModel):
    name: str
    storage_path: str
