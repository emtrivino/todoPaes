from fastapi import APIRouter

from app.schemas.diagnostic import DiagnosticOut
from app.services.diagnostic_service import DiagnosticService

router = APIRouter()


@router.get("/estimate", response_model=DiagnosticOut)
def estimate_score(accuracy: float = 0.0):
    return DiagnosticOut(estimated_score=DiagnosticService.estimate_from_accuracy(accuracy))
