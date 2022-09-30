import requests, re
from bs4 import BeautifulSoup as soup
from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional
from lib.otakudesu import Otakudesu
from api.models.otakudesusch import OtakudesuSchema

AUTHOR = "Sandy Sayang Gawr Gura"

ROUTER = APIRouter()

responses = {
    404: {
        "description": "Not found!",
        "content": {
            "application/json": {
                "example": {"author": AUTHOR, "status": 404, "message": "Not found!"}
            }
        },
    },
    406: {
        "description": "Invalid URL!",
        "content": {
            "application/json": {
                "example": {
                    "author": AUTHOR,
                    "status": 406,
                    "message": "Invalid query!",
                }
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
    "/otakudesu",
    response_model=OtakudesuSchema,
    responses={
        **responses,
        200: {
            "description": "Successfully response",
            "content": {
                "application/json": {
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
										"size": "File size"
									},
								],
								"sd_480p": [
									{
										"name": "File hosting name",
										"url": "File URL",
										"size": "File size"
									},
								],
								"hd_720p": [
									{
										"name": "File hosting name",
										"url": "File URL",
										"size": "File size"
									},
								],
							}
							
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
										"size": "File size"
									},
								],
								"sd_480p": [
									{
										"name": "File hosting name",
										"url": "File URL",
										"size": "File size"
									},
								],
								"hd_720p": [
									{
										"name": "File hosting name",
										"url": "File URL",
										"size": "File size"
									},
								],
							}
							
                        }
                    }
                }
            },
        },
    },
    summary="Otakudesu scraper",
)
async def otakudesu(query: Optional[str] = Query(None)):
    """
    Otakudesu scraper API
    """
    if not query:
        return JSONResponse(
            status_code=406,
            content=jsonable_encoder(
                {"author": AUTHOR, "status": 406, "message": "Invalid query"}
            ),
        )
    if Otakudesu(query):
        return JSONResponse(
            status_code=200,
            content=jsonable_encoder(
                {"author": AUTHOR, "status": 200, **Otakudesu(query)}
            ),
        )
    else:
        return JSONResponse(
            status_code=404,
            content=jsonable_encoder(
                {"author": AUTHOR, "status": 404, "message": "Not found!"}
            ),
        )
