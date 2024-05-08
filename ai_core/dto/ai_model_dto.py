from pydantic import BaseModel


class LargeLanguageModelDTO(BaseModel):
    name: str
    source: str
