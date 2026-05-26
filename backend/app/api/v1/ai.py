from fastapi import APIRouter

from app.schemas.ai import AIFeedbackOut
from app.services.ai_feedback_service import AIFeedbackService

router = APIRouter()
service = AIFeedbackService()


@router.get("/feedback", response_model=AIFeedbackOut)
def quick_feedback(correct: bool = False):
    msg = service.generate_question_feedback(question=None, selected_option="", is_correct=correct)
    return AIFeedbackOut(message=msg)
