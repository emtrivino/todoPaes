from fastapi import APIRouter

from app.schemas.career import CareerSimulationIn, CareerSimulationOut
from app.services.career_simulator_service import calculate_weighted_score

router = APIRouter()


@router.post("/simulate", response_model=CareerSimulationOut)
def simulate(payload: CareerSimulationIn):
    score = calculate_weighted_score(payload.scores, payload.weights)
    return CareerSimulationOut(weighted_score=score)
