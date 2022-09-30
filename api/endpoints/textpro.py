import requests, re
from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional
from lib.data import effect
from lib.textmaker import Textpro
from api.models.textprosch import TextproSchema

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
        "description": "The text or ID what you given is invalid!",
        "content": {
            "application/json": {
                "example": {
                    "author": AUTHOR,
                    "status": 406,
                    "message": "Invalid text or ID",
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
    "/textpro",
    response_model=TextproSchema,
    responses={
        **responses,
        200: {
            "description": "Successfully response",
            "content": {
                "application/json": {
                    "example": {
                        "author": AUTHOR,
                        "status": 200,
                        "title": "Title of image",
                        "url": "Result of image",
                    }
                }
            },
        },
    },
    summary="Textpro.me Scraper",
)
async def textpro(id: Optional[int] = Query(None), text: Optional[str] = Query(None)):
    """
    Create text image based Textpro.me. Available ID: 1 - 101
    """
    if not type(id) is int or not id or not text:
        return JSONResponse(
            status_code=404,
            content=jsonable_encoder(
                {"author": AUTHOR, "status": 404, "message": "Not found!"}
            ),
        )
    if effect(id - 1):
        res = Textpro(effect(id - 1), text)
        return JSONResponse(
            status_code=200,
            content=jsonable_encoder({"author": AUTHOR, "status": 200, **res}),
        )
    else:
        return JSONResponse(
            status_code=406,
            content=jsonable_encoder(
                {"author": AUTHOR, "status": 406, "message": "Invalid text or ID"}
            ),
        )
