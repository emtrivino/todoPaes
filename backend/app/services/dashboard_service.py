from sqlalchemy.orm import Session

from app.models.attempt import Attempt


class DashboardService:
    @staticmethod
    def build_summary(db: Session, user_id: int) -> dict:
        attempts = db.query(Attempt).filter_by(user_id=user_id).all()
        total = len(attempts)
        correct = sum(1 for attempt in attempts if attempt.is_correct)
        accuracy = (correct / total) if total else 0.0
        return {"total_attempts": total, "correct_attempts": correct, "accuracy": round(accuracy, 4)}
