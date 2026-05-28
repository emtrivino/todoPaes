from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app import models  # noqa: F401
from app.api.v1.router import api_router
from app.core.config import settings
from app.core.database import Base, engine
from app.web.router import web_router

app = FastAPI(title=settings.APP_NAME)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

static_dir = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=static_dir), name="static")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "todopaes-backend"}


app.include_router(web_router)
app.include_router(api_router, prefix="/api/v1")
