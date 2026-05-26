from sqlalchemy.orm import Session

from app.models.question import Question


class QuestionService:
    @staticmethod
    def list_active_questions(db: Session, limit: int = 20) -> list[Question]:
        return db.query(Question).filter(Question.is_active.is_(True)).limit(limit).all()
