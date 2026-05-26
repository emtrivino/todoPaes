from pydantic import BaseModel


class AIFeedbackOut(BaseModel):
    message: str
