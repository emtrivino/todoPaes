from sqlalchemy import JSON, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(String, nullable=False)
    options = Column(JSON, nullable=False)
    correct_option = Column(String, nullable=False)
    explanation = Column(String, nullable=True)
    difficulty = Column(String, default="media", nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)
    topic_id = Column(Integer, ForeignKey("topics.id"), nullable=True)

    subject = relationship("Subject", back_populates="questions")
    topic = relationship("Topic", back_populates="questions")
    attempts = relationship("Attempt", back_populates="question")
