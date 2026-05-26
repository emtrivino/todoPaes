from app.models.user import User
from app.repositories.base import BaseRepository


class UserRepository(BaseRepository):
    def get_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter_by(email=email).first()
