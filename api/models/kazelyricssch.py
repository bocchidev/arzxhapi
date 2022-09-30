from pydantic import BaseModel, HttpUrl
from typing import Dict

AUTHOR = "Sandy Sayang Gawr Gura"


class KazelyricsResultsSchema(BaseModel):
    title: str
    url: HttpUrl
    thumbnail: HttpUrl
    lyrics: str


class KazelyricsSchema(BaseModel):
    author: str
    status: int
    results: list[KazelyricsResultsSchema] 

    class Config:
        schema_extra = {
            "example": {
                "author": AUTHOR,
                "status": 200,
                "results": [
                    {
                        "title": "Song title",
                        "url": "Song URL",
                        "thumbnail": "Song thumbnail",
                        "lyrics": "Song lyrics"
                    },
                ]
            }
        }
