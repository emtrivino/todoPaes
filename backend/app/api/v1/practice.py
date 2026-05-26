from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, get_db
from app.models.attempt import Attempt
from app.models.question import Question
from app.schemas.practice import PracticeResultOut
from app.schemas.question import AnswerIn

router = APIRouter()


@router.post("/{question_id}/answer", response_model=PracticeResultOut)
def answer_question(question_id: int, payload: AnswerIn, db: Session = Depends(get_db), user=Depends(get_current_user)):
    question = db.query(Question).filter_by(id=question_id, is_active=True).first()
    if not question:
        raise HTTPException(status_code=404, detail="Pregunta no encontrada")

    is_correct = payload.selected_option == question.correct_option
    attempt = Attempt(
        user_id=user.id,
        question_id=question_id,
        selected_option=payload.selected_option,
        is_correct=is_correct,
    )
    db.add(attempt)
    db.commit()

    return PracticeResultOut(question_id=question_id, is_correct=is_correct, explanation=question.explanation)
