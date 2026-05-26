from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.question import QuestionOut
from app.services.question_service import QuestionService

router = APIRouter()


@router.get("", response_model=list[QuestionOut])
def list_questions(limit: int = 20, db: Session = Depends(get_db)):
    return QuestionService.list_active_questions(db, limit=limit)
