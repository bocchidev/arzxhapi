from pydantic import BaseModel, HttpUrl

AUTHOR = "Sandy Sayang Gawr Gura"


class TinyURLSchema(BaseModel):
    author: str
    status: int
    url: HttpUrl

    class Config:
        schema_extra = {
            "example": {"author": AUTHOR, "status": 200, "url": "https://tinyurl.com/"}
        }
