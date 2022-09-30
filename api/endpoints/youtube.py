import requests, re
from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional
from pytube import YouTube
from hurry.filesize import size, alternative
from api.models.youtubesch import YouTubeSchema

AUTHOR = "Sandy Sayang Gawr Gura"

ROUTER = APIRouter()

responses = {
    404: {
        "description": "Not found!",
        "content": {
            "application/json": {
                "example": {
                    "author": AUTHOR,
                    "status": 404,
                    "message": "URL not found!",
                }
            }
        },
    },
    406: {
        "description": "Invalid URL!",
        "content": {
            "application/json": {
                "example": {"author": AUTHOR, "status": 406, "message": "Invalid URL!"}
            }
        },
    },
    422: {
        "description": "Unprocessable",
        "content": {
            "application/json": {
                "example": {
                    "author": AUTHOR,
                    "status": 422,
                    "message": "Unprocessable request!",
                }
            }
        },
    },
}


@ROUTER.get(
    "/youtube",
    response_model=YouTubeSchema,
    responses={
        **responses,
        200: {
            "description": "Successfully response",
            "content": {
                "application/json": {
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
            },
        },
    },
    summary="YouTube Downloader",
)
async def youtube(url: Optional[str] = Query(None)):
    """
    Download video and audio from YouTube
    """
    if not re.search(r"http[s]\:\/\/", url):
        return JSONResponse(
            status_code=406,
            content=jsonable_encoder(
                {"author": AUTHOR, "status": 406, "message": "Invalid URL"}
            ),
        )
    data = YouTube(url)
    if data:
        raw = data.vid_info
        resAudio = raw["streamingData"]["adaptiveFormats"]
        resAudio = [a for a in resAudio if a["itag"] == 140][0]
        resVideo = raw["streamingData"]["formats"]
        resVideo = [b for b in resVideo if b["itag"] == 22][0]
        results = {
            "author": AUTHOR,
            "status": 200,
            "title": data.title,
            "description": data.description,
            "thumbnail": data.thumbnail_url,
            "audio": {
                "url": resAudio["url"],
                "size": size(
                    data.streams.get_by_itag(140).filesize, system=alternative
                ),
                "mimeType": resAudio["mimeType"],
            },
            "video": {
                "url": resVideo["url"],
                "size": size(data.streams.get_by_itag(22).filesize, system=alternative),
                "mimeType": resVideo["mimeType"],
            },
        }
        return JSONResponse(status_code=200, content=jsonable_encoder(results))
    else:
        return JSONResponse(
            status_code=404,
            content=jsonable_encoder(
                {"author": AUTHOR, "status": 404, "message": "Not found!"}
            ),
        )
