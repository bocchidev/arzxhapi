from pydantic import BaseModel, HttpUrl

AUTHOR = "Sandy Sayang Gawr Gura"


class KusonimeDownloadSchema(BaseModel):
    sd: list[HttpUrl]
    hd: list[HttpUrl]


class KusonimeInfoSchema(BaseModel):
    japanese: str
    genres: str
    seasons: str
    producers: str
    types: str
    status: str
    total_episodes: str
    scores: str
    duration: str
    released_on: str


class KusonimeResultsSchema(BaseModel):
    title: str
    url: HttpUrl
    thumbnail: HttpUrl | None = None
    description: str
    info: KusonimeInfoSchema
    download: KusonimeDownloadSchema


class KusonimeSchema(BaseModel):
    author: str
    status: int
    results: list[KusonimeResultsSchema]

    class Config:
        schema_extra = {
            "example": {
                "author": AUTHOR,
                "status": 200,
                "results": [
                    {
                        "title": "Post title",
                        "url": "Post URL",
                        "thumbnail": "Post thumbnail",
                        "description": "Post description",
                        "info": {
                            "japanese": "Japanese anime title",
                            "genres": "Anime genre",
                            "seasons": "Anime seasons",
                            "producers": "Anime producers",
                            "types": "Anime type",
                            "status": "Anime status",
                            "total_episodes": "Total anime episodes",
                            "scores": "Anime scores",
                            "duration": "Anime duration",
                            "released_on": "Anime release",
                        },
                        "dwonload": {
                            "sd": ["SD resolution URLs"],
                            "hd": ["HD resolution URLs"],
                        },
                    }
                ],
            }
        }
