from app.core.database import SessionLocal
from fastapi import Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt,JWTError
from app.core.config import settings
from app.models.user import User
from sqlalchemy.orm import Session

oauth2=OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")
def get_db():
 db=SessionLocal();
 try: yield db
 finally: db.close()
def get_current_user(token:str=Depends(oauth2),db:Session=Depends(get_db)):
  try: email=jwt.decode(token,settings.SECRET_KEY,algorithms=["HS256"]).get("sub")
  except JWTError: raise HTTPException(401,"Token inválido")
  user=db.query(User).filter_by(email=email).first()
  if not user: raise HTTPException(401,"Usuario no encontrado")
  return user
