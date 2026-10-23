from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from gliner2 import GLiNER2

from app.config import get_settings
from app.routers import data, hello

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.model = GLiNER2.from_pretrained(settings.model_id)
    yield


app = FastAPI(title=settings.app_name, lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(hello.router)
app.include_router(data.router)
