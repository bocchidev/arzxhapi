from pydantic import BaseModel, HttpUrl

AUTHOR = "Sandy Sayang Gawr Gura"


class OtakudesuInfoSchema(BaseModel):
    title: str
    japanese: str
    score: str
    producer: str
    types: str
    status: str
    total_episodes: int
    duration: str
    release: str
    studio: str
    genres: str

		
class OtakudesuDownloadURLSchema(BaseModel):
    name: str
    url: HttpUrl
    size: str
		

class OtakudesuDownloadSchema(BaseModel):
    sd_360p: list[OtakudesuDownloadURLSchema]
    sd_480p: list[OtakudesuDownloadURLSchema]
    hd_720p: list[OtakudesuDownloadURLSchema]

		
class OtakudesuEpisodeSchema(BaseModel):
    title: str
    url: HttpUrl
    upload: str
    download: OtakudesuDownloadSchema
        
        
class OtakudesuBatchSchema(BaseModel):
    url: HttpUrl
    upload: str
    download: OtakudesuDownloadSchema
        

class OtakudesuSchema(BaseModel):
    author: str
    status: int
    title: str
    url: HttpUrl
    thumbnail: HttpUrl
    info: OtakudesuInfoSchema
    batch: OtakudesuBatchSchema
    episode: OtakudesuEpisodeSchema

    class Config:
        schema_extra = {
            "example": {
                "author": AUTHOR,
                "status": 200,
                "title": "Post title",
                "url": "Post URL",
                "thumbnail": "Post thumbnail",
                "info": {
                    "title": "Anime title",
                    "japanese": "Japanese anime title",
                    "score": "Anime score",
                    "producer": "Anime producers",
                    "types": "Anime type",
                    "status": "Anime status",
                    "total_episodes": "Total anime episodes",
                    "duration": "Anime duration",
                    "release": "Anime release",
                    "studio": "Anime studio",
                    "genres": "Anime genre",
                },
                "batch": {
                    "url": "Anime batch URL",
                    "upload": "Anime batch upload date",
                    "download": {
                        "sd_360p": [
                            {
                                "name": "File hosting name",
                                "url": "File URL",
                                "size": "File size",
                            },
                        ],
                        "sd_480p": [
                            {
                                "name": "File hosting name",
                                "url": "File URL",
                                "size": "File size",
                            },
                        ],
                        "hd_720p": [
                            {
                                "name": "File hosting name",
                                "url": "File URL",
                                "size": "File size",
                            },
                        ],
                    },
                },
                "episode": {
                    "title": "Anime episode title",
                    "url": "Anime episode URL",
                    "upload": "Anime episode upload date",
                    "download": {
                        "sd_360p": [
                            {
                                "name": "File hosting name",
                                "url": "File URL",
                                "size": "File size",
                            },
                        ],
                        "sd_480p": [
                            {
                                "name": "File hosting name",
                                "url": "File URL",
                                "size": "File size",
                            },
                        ],
                        "hd_720p": [
                            {
                                "name": "File hosting name",
                                "url": "File URL",
                                "size": "File size",
                            },
                        ],
                    },
                },
            }
        }
