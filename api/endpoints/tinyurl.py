import requests, re
from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional
from api.models.tinyurlsch import TinyURLSchema

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
    "/tinyurl",
    response_model=TinyURLSchema,
    responses={
        **responses,
        200: {
            "description": "Successfully response",
            "content": {
                "application/json": {
                    "example": {
                        "author": AUTHOR,
                        "status": 200,
                        "url": "https://tinyurl.com/",
                    }
                }
            },
        },
    },
    summary="URL Shortener",
)
async def tinyurl(url: Optional[str] = Query(None)):
    """
    Create short URL based TinyURL
    """
    if not re.search(r"http[s]\:\/\/", url):
        return JSONResponse(
            status_code=406,
            content=jsonable_encoder(
                {"author": AUTHOR, "status": 406, "message": "Invalid URL"}
            ),
        )
    data = requests.get("https://tinyurl.com/api-create.php", params={"url": url}).text
    if data:
        return JSONResponse(
            status_code=200,
            content=jsonable_encoder({"author": AUTHOR, "status": 200, "url": data}),
        )
    else:
        return JSONResponse(
            status_code=404,
            content=jsonable_encoder(
                {"author": AUTHOR, "status": 404, "message": "Not found!"}
            ),
        )
