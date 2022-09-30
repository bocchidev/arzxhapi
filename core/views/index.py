from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

ROUTER = APIRouter()

ROUTER.mount("/static", StaticFiles(directory="static"), name="static")

TEMPLATES = Jinja2Templates(directory="public")


@ROUTER.get("/", response_class=HTMLResponse, summary="Home page")
async def root(request: Request):
    """
    Return the main page of this web
    """
    return TEMPLATES.TemplateResponse("index.html", {"request": request})
