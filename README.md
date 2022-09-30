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

## Add endpoints
To add endpoints, create new file in <code>/api/endpoints</code>
<p>Example endpoints:</p>
```python
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

## Support
You can support me via <a href="https://trakteer.id/arzhav/tip">Trakteer</a>
