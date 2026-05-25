from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1.router import api_router
from app.core.database import Base, engine
from app import models

app=FastAPI(title=settings.APP_NAME)
app.add_middleware(CORSMiddleware,allow_origins=[settings.FRONTEND_URL],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])
Base.metadata.create_all(bind=engine)
@app.get("/health")
def health(): return {"status":"ok","service":"todopaes-backend"}
app.include_router(api_router,prefix="/api/v1")
