class GamificationService:
    @staticmethod
    def streak_badge(streak_days: int) -> str:
        if streak_days >= 30:
            return "legendario"
        if streak_days >= 7:
            return "constante"
        if streak_days >= 1:
            return "en_racha"
        return "inicio"
