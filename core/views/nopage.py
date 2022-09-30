from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

ROUTER = APIRouter()

ROUTER.mount("/static", StaticFiles(directory="static"), name="static")

TEMPLATES = Jinja2Templates(directory="public")


@ROUTER.get("/{id}", response_class=HTMLResponse, summary="Validate main parameter")
async def Page_Validate(request: Request):
    """
    Validate all parameter. If not found parameter, return not found page exception.
    """
    return TEMPLATES.TemplateResponse("nopage.html", {"request": request})
