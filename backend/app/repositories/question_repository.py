from app.models.question import Question
from app.repositories.base import BaseRepository


class QuestionRepository(BaseRepository):
    def list_active(self, limit: int = 20) -> list[Question]:
        return self.db.query(Question).filter(Question.is_active.is_(True)).limit(limit).all()
