from app.models.attempt import Attempt
from app.repositories.base import BaseRepository


class AttemptRepository(BaseRepository):
    def create(self, **kwargs) -> Attempt:
        attempt = Attempt(**kwargs)
        self.db.add(attempt)
        self.db.commit()
        self.db.refresh(attempt)
        return attempt
