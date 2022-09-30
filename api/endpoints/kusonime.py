import requests, re
from bs4 import BeautifulSoup as soup
from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional
from lib.kusonime import Kusonime
from api.models.kusonimesch import KusonimeSchema

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
    "/kusonime",
    response_model=KusonimeSchema,
    responses={
        **responses,
        200: {
            "description": "Successfully response",
            "content": {
                "application/json": {
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
                                "download": {
                                    "sd": ["SD resolution URLs"],
                                    "hd": ["HD resolution URLs"],
                                },
                            }
                        ],
                    }
                }
            },
        },
    },
    summary="Kusonime scraper",
)
async def kusonime(query: Optional[str] = Query(None)):
    """
    Kusonime.com scraper
    """
    if not query:
        return JSONResponse(
            status_code=406,
            content=jsonable_encoder(
                {"author": AUTHOR, "status": 406, "message": "Invalid query"}
            ),
        )
    if Kusonime(query):
        results = Kusonime(query)
        return JSONResponse(
            status_code=200,
            content=jsonable_encoder(
                {"author": AUTHOR, "status": 200, "results": results}
            ),
        )
    else:
        return JSONResponse(
            status_code=404,
            content=jsonable_encoder(
                {"author": AUTHOR, "status": 404, "message": "Not found!"}
            ),
        )
