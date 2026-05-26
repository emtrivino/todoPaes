from app.core.database import Base, SessionLocal, engine
from app.core.security import hash_password
from app.models.user import User
from app.seed.m1_questions_seed import seed_m1_questions


def main():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        if not db.query(User).filter_by(email="demo@todopaes.cl").first():
            db.add(
                User(
                    email="demo@todopaes.cl",
                    full_name="Demo TodoPAES",
                    hashed_password=hash_password("demo1234"),
                )
            )
            db.commit()

        seed_m1_questions(db)
        print("seed ok")
    finally:
        db.close()


if __name__ == "__main__":
    main()
