from app.services.scoring_service import estimate_paes_score


class DiagnosticService:
    @staticmethod
    def estimate_from_accuracy(accuracy: float) -> int:
        return estimate_paes_score(accuracy)
