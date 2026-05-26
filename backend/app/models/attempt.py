from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class Attempt(Base):
    __tablename__ = "attempts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)
    selected_option = Column(String, nullable=False)
    is_correct = Column(Boolean, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    user = relationship("User")
    question = relationship("Question", back_populates="attempts")
