import argparse
from pathlib import Path

from sqlalchemy.exc import OperationalError

from app.core.database import Base, SessionLocal, engine
from app.core.security import hash_password
from app.models.user import User
from app.seed.m1_questions_seed import seed_m1_questions

DB_PATH = Path("todopaes.db")


def main() -> None:
    parser = argparse.ArgumentParser(description="Seed local TodoPAES database")
    parser.add_argument("--reset", action="store_true", help="Delete local sqlite DB before creating schema")
    args = parser.parse_args()

    if args.reset and DB_PATH.exists():
        DB_PATH.unlink()
        print("Removed existing database: todopaes.db")

    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        try:
            demo_user = db.query(User).filter_by(email="demo@todopaes.cl").first()
        except OperationalError:
            print("Schema mismatch detected in local SQLite database.")
            print("Run: python -m app.seed.seed_data --reset")
            return

        if not demo_user:
            db.add(
                User(
                    email="demo@todopaes.cl",
                    full_name="Demo TodoPAES",
                    hashed_password=hash_password("demo1234"),
                )
            )
            db.commit()

        seed_m1_questions(db)
        print("Seed completed successfully.")
    finally:
        db.close()


if __name__ == "__main__":
    main()
