# ARZXHAPI
My REST API project

## Clone
To clone this repo, paste code below
```sh
git clone https://github.com/KurniawanIDX/arzxhapi && cd arzxhapi
```

## Install
To install this repo to your local server
```sh
pip install -r requirements.txt && python main.py
```

## Add endpoints and models
To add endpoints, create new file in <code>/api/endpoints</code> and create model in <code>/api/model</code>
<p>Example endpoints:</p>
```python
import requests, re
from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional
from api.models.foo import foo #example model

AUTHOR = "Sandy Sayang Gawr Gura" #Author

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
                "example": {"author": AUTHOR, "status": 406, "message": "Invalid input!"}
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
    "/foo", #Your endpoints name
    response_model=foo, #example model
    responses={
        **responses,
        200: {
            "description": "Successfully response",
            "content": {
                "application/json": {
                    "example": {
                        "author": AUTHOR,
                        "status": 200,
                        "foo": "Hello world!", #Example response
                    }
                }
            },
        },
    },
    summary="Foo", #Your endpoints summary
)
async def foo(bar: Optional[str] = Query(None)):
    """
    Lorem ipsum
    """ #Your endpoints description
    if not re.search(bar): #logic here
        return JSONResponse(
            status_code=406,
            content=jsonable_encoder(
                {"author": AUTHOR, "status": 406, "message": "Invalid input"} 
            ),
        )
    if data: #logic here
        return JSONResponse(
            status_code=200,
            content=jsonable_encoder({"author": AUTHOR, "status": 200, "bar": "Hello world!"}),
        )
    else: #logic here
        return JSONResponse(
            status_code=404,
            content=jsonable_encoder(
                {"author": AUTHOR, "status": 404, "message": "Not found!"}
            ),
        )

```

<p>Example model</p>
```python
from pydantic import BaseModel

AUTHOR = "Sandy Sayang Gawr Gura" #Author


class TinyURLSchema(BaseModel): #Your model
    author: str
    status: int
    bar: str

    class Config:
        schema_extra = {
            "example": {"author": AUTHOR, "status": 200, "bar": "Hello world"}
        }
```

## Support
You can support me via <a href="https://trakteer.id/arzhav/tip">Trakteer</a>
