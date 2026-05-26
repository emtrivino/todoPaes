from pydantic import BaseModel


class CareerSimulationIn(BaseModel):
    scores: dict[str, float]
    weights: dict[str, float]


class CareerSimulationOut(BaseModel):
    weighted_score: float
