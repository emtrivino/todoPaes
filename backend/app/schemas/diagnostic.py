from pydantic import BaseModel


class DiagnosticOut(BaseModel):
    estimated_score: int
