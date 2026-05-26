from app.models.question import Question
from app.models.subject import Subject
from app.models.topic import Topic


def seed_m1_questions(db):
    subject = db.query(Subject).filter_by(code="M1").first()
    if not subject:
        subject = Subject(code="M1", name="Matemática M1")
        db.add(subject)
        db.flush()

    topic = db.query(Topic).filter_by(name="Álgebra", subject_id=subject.id).first()
    if not topic:
        topic = Topic(name="Álgebra", subject_id=subject.id)
        db.add(topic)
        db.flush()

    if not db.query(Question).filter_by(subject_id=subject.id).first():
        db.add(
            Question(
                prompt="Si x + 3 = 8, ¿cuál es x?",
                options=["3", "5", "8", "11"],
                correct_option="5",
                explanation="Resta 3 en ambos lados.",
                subject_id=subject.id,
                topic_id=topic.id,
            )
        )
        db.commit()
