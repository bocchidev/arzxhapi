import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from api import ROUTER
from core import ROOT

app = FastAPI(
    title="ARZXH API",
    version="0.0.1",
    description="A free REST API built for the convenience of all.  No API key required and no fees, it\'s all free for you.",
    openapi_url="/openapi.json"
    )

ORIGINS = ["https://localhost:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(ROOT)
app.include_router(ROUTER)

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)