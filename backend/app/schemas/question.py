from pydantic import BaseModel


class QuestionOut(BaseModel):
    id: int
    prompt: str
    options: list[str]
    difficulty: str
    subject_id: int
    topic_id: int | None = None

    class Config:
        from_attributes = True


class AnswerIn(BaseModel):
    selected_option: str
