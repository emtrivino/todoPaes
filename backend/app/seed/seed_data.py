from app.core.database import Base,engine,SessionLocal
from app.models.user import User
from app.core.security import hash_password

def main():
 Base.metadata.create_all(bind=engine)
 db=SessionLocal()
 if not db.query(User).filter_by(email='demo@todopaes.cl').first():
  db.add(User(email='demo@todopaes.cl',full_name='Demo TodoPAES',hashed_password=hash_password('demo1234')));db.commit()
 print('seed ok')

if __name__=='__main__': main()
