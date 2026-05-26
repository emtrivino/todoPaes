from pydantic import BaseModel


class DashboardOut(BaseModel):
    total_attempts: int
    correct_attempts: int
    accuracy: float
