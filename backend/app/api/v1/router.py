from fastapi import APIRouter

from . import ai, auth, careers, dashboard, diagnostics, practice, questions, subjects, users

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(subjects.router, prefix="/subjects", tags=["subjects"])
api_router.include_router(questions.router, prefix="/questions", tags=["questions"])
api_router.include_router(practice.router, prefix="/practice", tags=["practice"])
api_router.include_router(ai.router, prefix="/ai", tags=["ai"])
api_router.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])
api_router.include_router(diagnostics.router, prefix="/diagnostics", tags=["diagnostics"])
api_router.include_router(careers.router, prefix="/careers", tags=["careers"])
