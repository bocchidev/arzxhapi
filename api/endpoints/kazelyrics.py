import requests, re
from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional
from lib.kazelyrics import Kazelyrics
from api.models.kazelyricssch import KazelyricsSchema

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
                    "message": "Not found!",
                }
            }
        },
    },
    406: {
        "description": "Invalid URL!",
        "content": {
            "application/json": {
                "example": {"author": AUTHOR, "status": 406, "message": "Invalid query!"}
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
    "/kazelyrics",
    response_model=KazelyricsSchema,
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
                                "title": "Song title",
                                "url": "Song URL",
                                "thumbnail": "Song thumbnail",
                                "lyrics": "Song lyrics"
                            }
                        ]
                    }
                }
            },
        },
    },
    summary="Kazelyrics scraper",
)
async def kazelyrics(query: Optional[str] = Query(None)):
    """
    Find your favorite Japanese song in Kazelyrics
    """
    if not query:
        return JSONResponse(
            status_code=406,
            content=jsonable_encoder(
                {"author": AUTHOR, "status": 406, "message": "Invalid URL"}
            ),
        )
    if Kazelyrics(query):
        return JSONResponse(
            status_code=200,
            content=jsonable_encoder({"author": AUTHOR, "status": 200, "results": Kazelyrics(query)}),
        )
    else:
        return JSONResponse(
            status_code=404,
            content=jsonable_encoder(
                {"author": AUTHOR, "status": 404, "message": "Not found!"}
            ),
        )
