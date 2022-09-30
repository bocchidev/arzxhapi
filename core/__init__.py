from fastapi import APIRouter
from .views import index
from .views import nopage

ROOT = APIRouter(
    tags=["HOME PAGE"]
)

ROOT.include_router(index.ROUTER)
ROOT.include_router(nopage.ROUTER)