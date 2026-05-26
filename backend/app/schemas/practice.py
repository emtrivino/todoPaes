from pydantic import BaseModel


class PracticeResultOut(BaseModel):
    question_id: int
    is_correct: bool
    explanation: str | None = None
