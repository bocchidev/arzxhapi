from pydantic import BaseModel, HttpUrl
from typing import Dict

AUTHOR = "Sandy Sayang Gawr Gura"


class YouTubeResultURLSchema(BaseModel):
    url: HttpUrl
    size: str
    mimeType: str


class YouTubeSchema(BaseModel):
    author: str
    status: int
    title: str
    description: str
    thumbnail: HttpUrl
    audio: YouTubeResultURLSchema
    video: YouTubeResultURLSchema

    class Config:
        schema_extra = {
            "example": {
                "author": AUTHOR,
                "status": 200,
                "title": "Judul video",
                "description": "Deskripsi video",
                "thumbnail": "URL thumbnail video",
                "audio": {
                    "url": "URL unduhan",
                    "size": "Ukuran audio",
                    "mimeType": "MymeType audio",
                },
                "video": {
                    "url": "URL unduhan",
                    "size": "Ukuran video",
                    "mimeType": "MymeType video",
                },
            }
        }
