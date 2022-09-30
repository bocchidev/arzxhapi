from pydantic import BaseModel, HttpUrl

AUTHOR = "Sandy Sayang Gawr Gura"


class TextproSchema(BaseModel):
    author: str
    status: int
    title: str
    url: HttpUrl

    class Config:
        schema_extra = {
            "example": {
                "author": "Sandy Sayang Gawr Gura",
                "status": 200,
                "title": "Judul gambar",
                "url": "URL gambar",
            }
        }
